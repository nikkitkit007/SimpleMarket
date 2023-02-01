from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, TEXT

from data_base import DeclarativeBase
from data_base.table_config import TBL_PRODUCT
import json


class Product(DeclarativeBase):
    __tablename__ = TBL_PRODUCT

    id = Column(
        INTEGER,
        primary_key=True,
        unique=True,
        doc="Unique id of product",
    )
    name = Column(
        TEXT,
        nullable=False,
        doc="Name of product",
    )
    manufacturer = Column(
        TEXT,
        nullable=False,
        unique=True,
        doc="Manufacturer of product",
    )
    price = Column(
        INTEGER,
        nullable=False,
        doc="Price of product",
    )

    def to_dict(self, exclude_keys: list) -> dict:
        base = self.__dict__
        base.pop("_sa_instance_state", None)

        for e_key in exclude_keys:
            base.pop(e_key, None)

        return base

    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'{", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}'
