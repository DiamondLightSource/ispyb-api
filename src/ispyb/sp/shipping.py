# shipping.py
#
#    Copyright (C) 2017 Diamond Light Source, Karl Levik
#
# 2017-06-28
#
# Methods to update data related to shipping of samples
#

import copy

import ispyb.interface.shipping
from ispyb.strictordereddict import StrictOrderedDict


class Shipping(ispyb.interface.shipping.IF):
    """Shipping provides methods to update shipments and samples."""

    def __init__(self):
        pass

    _dewar_params = StrictOrderedDict(
        [
            ("id", None),
            ("authLogin", None),
            ("shippingId", None),
            ("name", None),
            ("comments", None),
            ("storageLocation", None),
            ("status", None),
            ("isStorageDewar", None),
            ("barCode", None),
            ("firstSessionId", None),
            ("customsValue", None),
            ("transportValue", None),
            ("trackingNumberToSynchrotron", None),
            ("trackingNumberFromSynchrotron", None),
            ("type", None),
            ("facilityCode", None),
            ("weight", None),
            ("deliveryAgentBarcode", None),
        ]
    )

    @classmethod
    def get_dewar_params(cls):
        return copy.deepcopy(cls._dewar_params)

    def update_container_assign(self, beamline, registry_barcode, position):
        """Assign a container"""
        return self.get_connection().call_sp_retrieve(
            procname="update_container_assign",
            args=(beamline, registry_barcode, position),
        )

    def update_container_unassign_all_for_beamline(self, beamline):
        """Unassign all containers for a given beamline. Assumes container.sessionId and container.containerRegistryId are populated."""
        self.get_connection().call_sp_write(
            procname="update_container_unassign_all_for_beamline", args=(beamline,)
        )

    def upsert_dewar(self, values):
        """Insert or update a dewar or parcel"""
        return self.get_connection().call_sp_write("upsert_dewar_v2", values)

    def retrieve_dewars_for_proposal_code_number(
        self, proposal_code, proposal_number, auth_login=None
    ):
        """Get a result-set with the dewars associated with shipments in a given proposal specified by proposal code, proposal_number"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_dewars_for_proposal_code_number_v2",
            args=(proposal_code, proposal_number, auth_login),
        )

    def retrieve_container_for_sample_id(self, sample_id, auth_login=None):
        """Get a single row result-set with the container info for the sample identified by sample_id"""
        return self.get_connection().call_sp_retrieve(
            procname="retrieve_container_for_sample_id", args=(sample_id, auth_login)
        )
