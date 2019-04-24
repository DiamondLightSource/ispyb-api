from __future__ import absolute_import, division, print_function


class PDB(object):
    """An object representing immutable values of a PDB database entry.
    In Python 3.7 this would probably be a much simpler @dataclass.
    """

    def __init__(self, name=None, rawfile=None, code=None):
        """Create a PDB object. It may have a user-defined name, it may contain
        a full PDB file, and it may refer to an official PDB entry.
        Most likely it will either contain a raw PDB file,
        or a 4 character PDB code.

        :param name: A user-defined name for this PDB entry
        :param rawfile: A string containing a full PDB file, or None
        :param code: A 4 character string referencing a PDB entry, or None
        """
        self._name = name
        self._rawfile = rawfile or None
        self._code = code or None

    @property
    def name(self):
        """Returns the user-defined PDB entry name."""
        return self._name

    @property
    def rawfile(self):
        """Returns the PDB file contents if such a file is present in the database.
        Otherwise, returns None.
        """
        return self._rawfile

    @property
    def code(self):
        """Returns the PDB entry code if such a code is set in the database.
        Otherwise, returns None.
        """
        return self._code

    def __repr__(self):
        """Returns an object representation, including the DataCollectionGroupID,
        the database connection interface object, and the cache status."""
        return "<PDB %s>" % (self._name,)

    def __str__(self):
        """Returns a pretty-printed object representation."""
        if self.rawfile is None:
            file_summary = "None"
        else:
            file_summary = "defined (%d bytes)" % len(self.rawfile)
        return (
            "\n".join(("PDB {0.name}", "  File: {file}", "  Code: {0.code}"))
        ).format(self, file=file_summary)
