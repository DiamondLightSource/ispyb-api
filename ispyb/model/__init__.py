import warnings

warnings.warn(
    "ispyb.model has been deprecated and will be removed in a future version. "
    "You can use the SQLAlchemy models in ispyb.sqlalchemy instead",
    DeprecationWarning,
    stacklevel=2,
)


class DBCache:
    """A helper class with useful functions to manage caching of database
    requests.
    Subclasses must implement reload() which should store data to be cached
    in self._data. Cached data should be accessed as self._data. On first
    uncached access reload() is called."""

    def load(self):
        """Ensure data is loaded from the database."""
        if not self.cached:
            self.reload()

    def reload(self):
        """Force update from the database."""
        raise NotImplementedError()

    @property
    def _data(self):
        """Internal caching logic so that information is only read once from the
        database, and only when required."""
        if not hasattr(self, "_data_cache"):
            self.reload()
        return getattr(self, "_data_cache")

    @_data.setter
    def _data(self, value):
        setattr(self, "_data_cache", value)

    @property
    def cached(self):
        return hasattr(self, "_data_cache")


class EncapsulatedValue:
    """A helper class encapsulating another object and mostly behaving as that
    object. The property .value allows access to the original object.
    A list of magic methods is implemented to allow meaningful comparisons.
    """

    def __init__(self, value):
        """Encapsulate an object."""
        self._value = value

    @property
    def value(self):
        """Provide read-only access to the encapsulated object"""
        return self._value

    def __getattr__(self, item):
        """Any undefined attribute access is passed to the encapsulated object."""
        return self._value.__getattr__(item)

    def __getitem__(self, item):
        """Default item getter for iteration."""
        return self._value.__getitem__(item)

    def __str__(self):
        """String coercion"""
        return self._value.__str__()

    def __eq__(self, other):
        """Equality operator (==)"""
        return self._value == other

    def __ne__(self, other):
        """Not-equals operator (!=)"""
        return self._value != other

    def __lt__(self, other):
        """Less-than operator (<)"""
        return self._value < other

    def __le__(self, other):
        """Less-than-or-equals operator (<=)"""
        return self._value <= other

    def __gt__(self, other):
        """Greater-than operator (>)"""
        return self._value > other

    def __ge__(self, other):
        """Greater-than-or-equals operator (>=)"""
        return self._value >= other

    def __bool__(self):
        """Python 3: value when used in bool() context."""
        return bool(self._value)

    def __nonzero__(self):
        """Python 2: value when used in bool() context."""
        return bool(self._value)

    def __hash__(self):
        """Pass on the hash value of the inner object."""
        return hash(self._value)


def add_properties(objectclass, property_list):
    """Generate class properties for a model that provide read-only access
    to elements from the internal ._data data structure.

    :param objectclass: The class to which properties should be added
    :param property_list: A list of property name + data structure key
                          + optional docstring tuples. Property names
                          then read from the given data structure keys.
    """
    for prop_item in property_list:
        key = prop_item[0]
        internalkey = prop_item[1]

        def model_attribute(self, k=internalkey):
            return self._data[k]

        if len(prop_item) > 2:
            model_attribute.__doc__ = prop_item[2]
        setattr(objectclass, key, property(model_attribute))
