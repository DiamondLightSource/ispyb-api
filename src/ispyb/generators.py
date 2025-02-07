
from __future__ import annotations

from collections.abc import Sequence

import inflect
from sqlacodegen.generators import DeclarativeGenerator
from sqlacodegen.models import RelationshipAttribute, RelationshipType
from sqlalchemy import (
    MetaData,
)
from sqlalchemy.engine import Connection, Engine


class DeclarativeIspybGenerator(DeclarativeGenerator):
    def __init__(
        self,
        metadata: MetaData,
        bind: Connection | Engine,
        options: Sequence[str],
        *,
        indentation: str = "    ",
        base_class_name: str = "Base",
    ):
        super().__init__(metadata, bind, options, indentation=indentation)
        self.base_class_name: str = base_class_name
        self.inflect_engine = inflect.engine()

    def generate_relationship_name(
        self,
        relationship: RelationshipAttribute,
        global_names: set[str],
        local_names: set[str],
    ) -> None:
        # Self referential reverse relationships
        preferred_name: str
        if (
            relationship.type
            in (RelationshipType.ONE_TO_MANY, RelationshipType.ONE_TO_ONE)
            and relationship.source is relationship.target
            and relationship.backref
            and relationship.backref.name
        ):
            preferred_name = relationship.backref.name + "_reverse"
        else:
            preferred_name = relationship.target.table.name

            if relationship.constraint:
                is_source = relationship.source.table is relationship.constraint.table
                if is_source or relationship.type not in (
                    RelationshipType.ONE_TO_ONE,
                    RelationshipType.ONE_TO_MANY,
                ):
                    column_names = [c.name for c in relationship.constraint.columns]
                    if len(column_names) == 1 and column_names[0].endswith("_id"):
                        preferred_name = column_names[0][:-3]

        relationship.name = preferred_name
