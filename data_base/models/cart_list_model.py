from sqlalchemy import Column, ForeignKey, UniqueConstraint
from sqlalchemy.dialects.postgresql import INTEGER, TEXT

from data_base import DeclarativeBase
from data_base.table_config import TBL_CARTLIST

import data_base.table_config as config


class CartList(DeclarativeBase):
    __tablename__ = TBL_CARTLIST
    __table_args__ = (UniqueConstraint('cart_id', 'product_id'),)

    id = Column(
        INTEGER,
        primary_key=True,
        nullable=False,
        doc="Id",
    )
    cart_id = Column(
        INTEGER,
        # primary_key=True,
        ForeignKey(f"{config.TBL_CART}.id"),
        nullable=False,
        doc="Id of the cart",
    )
    product_id = Column(
        INTEGER,
        # primary_key=True,
        ForeignKey(f"{config.TBL_PRODUCT}.id"),
        nullable=False,
        doc="Id of the product",
    )
    count = Column(
        INTEGER,
        nullable=False,
        default=1,
        doc="Count of products",
    )

    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
