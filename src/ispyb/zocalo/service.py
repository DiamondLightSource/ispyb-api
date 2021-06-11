import time
from typing import Any, Callable, NamedTuple, Optional, Union

import pkg_resources
import workflows.recipe.wrapper
from workflows.services.common_service import CommonService

import ispyb


class FunctionParameter(NamedTuple):
    rw: workflows.recipe.wrapper.RecipeWrapper
    message: dict[str, Any]
    parameters: Callable[[str], Any]
    transaction: int


class FunctionResult(NamedTuple):
    success: bool = False
    checkpoint: bool = False
    return_value: Union[int, str, float, None] = None


class ISPyB(CommonService):
    """A service that can write information to ISPyB."""

    # Human readable service name
    _service_name = "ISPyB service"

    # Logger name
    _logger_name = "ispyb.zocalo.service"

    # Name of the queue that will be listened to
    _queue_name = "ispyb"

    def initializing(self):
        """Subscribe the ISPyB connector queue. Received messages must be
        acknowledged. Prepare ISPyB database connection."""
        self.log.info(f"ISPyB connector v{ispyb.__version__} starting")

        self.ispyb_functions: dict[str, Callable] = {
            e.name: e.load()
            for e in pkg_resources.iter_entry_points("ispyb.zocalo.service.plugins")
        }
        self.log.debug("Loaded %d service functions", len(self.ispyb_functions))

        self.ispyb = ispyb.open()
        workflows.recipe.wrap_subscribe(
            self._transport,
            self._queue_name,
            self.receive_msg,
            acknowledgement=True,
            log_extender=self.extend_log,
            allow_non_recipe_messages=True,
        )

    def receive_msg(
        self,
        rw: Optional[workflows.recipe.wrapper.RecipeWrapper],
        header: dict[str, str],
        message: dict[str, Any],
    ) -> None:
        """Act on an incoming message."""

        if header.get("redelivered") == "true":
            # A redelivered message may just have been processed in a parallel instance,
            # which was connected to a different database server in the DB cluster. If
            # we were to process it immediately we could run into a DB synchronization
            # issue. Avoid this by giving the DB cluster a bit of time to settle.
            self.log.debug("Received redelivered message, holding for a second.")
            time.sleep(0.2)

        if not rw:
            # Incoming message is not a recipe message. Simple messages can be valid
            if (
                not isinstance(message, dict)
                or not message.get("parameters")
                or not message.get("content")
            ):
                self.log.error("Rejected invalid simple message")
                self._transport.nack(header)
                return
            self.log.debug("Received a simple message")

            # Create a wrapper-like object that can be passed to functions
            # as if a recipe wrapper was present.
            class RW_mock:
                def dummy(self, *args, **kwargs):
                    pass

            rw = RW_mock()
            rw.transport = self._transport
            rw.recipe_step = {"parameters": message["parameters"]}
            rw.environment = {"has_recipe_wrapper": False}
            rw.set_default_channel = rw.dummy
            rw.send = rw.dummy
            message = message["content"]

        command = rw.recipe_step["parameters"].get("ispyb_command")
        if not command:
            self.log.error("Received message does not contain a valid ISPyB command")
            rw.transport.nack(header)
            return

        if command not in self.ispyb_functions:
            self.log.error("Received unknown ISPyB command (%s)", command)
            rw.transport.nack(header)
            return

        txn = rw.transport.transaction_begin()
        rw.set_default_channel("output")

        result = self._call_function(command, rw, txn, message)

        if not result.success:
            rw.transport.transaction_abort(txn)
            rw.transport.nack(header)
            return

        if result.checkpoint:
            rw.checkpoint(
                result.return_value,
                delay=rw.recipe_step["parameters"].get("delay"),
                transaction=txn,
            )
        else:
            rw.send({"result": result.return_value}, transaction=txn)
        rw.transport.ack(header, transaction=txn)
        rw.transport.transaction_commit(txn)

    def _call_function(
        self,
        function_name: str,
        rw: workflows.recipe.wrapper.RecipeWrapper,
        txn: int,
        message,
    ) -> FunctionResult:
        """
        Delegate a call to a registered ISPyB service plugin function.

        The plugin function must accept exactly one argument of type
        FunctionParameter and return an object of type FunctionResult.
        """
        # TODO: this function will become public, but atm not 100% convinced that
        # the function does the right thing. Should be useful for evaluating lists
        # of commands and wrapped calls (ie. ZocaloBuffer table stuff)

        def parameters(parameter: str, *, replace_variables: bool = True) -> Any:
            if isinstance(message, dict):
                base_value = message.get(
                    parameter, rw.recipe_step["parameters"].get(parameter)
                )
            else:
                base_value = rw.recipe_step["parameters"].get(parameter)
            if (
                not replace_variables
                or not base_value
                or not isinstance(base_value, str)
                or "$" not in base_value
            ):
                return base_value
            for key in sorted(rw.environment, key=len, reverse=True):
                if "${" + key + "}" in base_value:
                    base_value = base_value.replace(
                        "${" + key + "}", str(rw.environment[key])
                    )
                # Replace longest keys first, as the following replacement is
                # not well-defined when one key is a prefix of another:
                if "$" + key in base_value:
                    base_value = base_value.replace("$" + key, str(rw.environment[key]))
            return base_value

        result: FunctionResult = self.ispyb_functions[function_name](
            FunctionParameter(
                rw=rw, message=message, parameters=parameters, transaction=txn
            )
        )

        store_result = rw.recipe_step["parameters"].get("store_result")
        if store_result:
            self.log.debug(
                f"Storing result {result.return_value!r} in environment variable '{store_result}'",
            )
            rw.environment[store_result] = result.return_value

        return result
