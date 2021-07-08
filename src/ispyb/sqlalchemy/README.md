This provides a set of [SQLAlchemy](https://www.sqlalchemy.org/) ORM models for the
[ISPyB database](https://github.com/DiamondLightSource/ispyb-database/).

Checkout the specific tag for a given `ispyb-database` version:
```bash
$ git clone -b v1.18.1 https://github.com/DiamondLightSource/ispyb-database.git
$ # or, if you have an existing copy of the repository:
$ git checkout v1.18.1
```

Apply the schema patch in `sqlacodegen.patch` to avoid circular foreign key references:
```bash
$ patch -p1 < ispyb-api/src/ispyb/sqlalchemy/sqlacodegen.patch
```

Then run the `ispyb-database` `build.sh` script to generate the database:
```bash
$ sh build.sh
```

Generate the models with [sqlacodegen](https://pypi.org/project/sqlacodegen/)
in `ispyb-api/src/ispyb/sqlalchemy/`:
```bash
sqlacodegen mysql+mysqlconnector://user:password@host:port/ispyb_build --noinflect --outfile _auto_db_schema.py
```

**The resulting `_auto_db_schema.py` should not be edited** (other than automatic
formatting with `black` or sorting of imports with `isort`). All models are imported
into and accessed via the `__init__.py`. Any modifications, e.g. injecting additional
relationships between models should be done here.
