from sqlalchemy import Column
from sqlalchemy.dialects.postgresql import INTEGER, TEXT

from data_base import DeclarativeBase
from data_base.table_config import TBL_CART


class Cart(DeclarativeBase):
    __tablename__ = TBL_CART

    id = Column(
        INTEGER,
        primary_key=True,
        unique=True,
        doc="Unique id of the cart",
    )
    count = Column(
        INTEGER,
        nullable=False,
        default=0,
        doc="Count of products",
    )
    price = Column(
        INTEGER,
        nullable=False,
        default=0,
        doc="Total price of cart",
    )

    def __repr__(self):
        columns = {column.name: getattr(self, column.name) for column in self.__table__.columns}
        return f'<{self.__tablename__}: {", ".join(map(lambda x: f"{x[0]}={x[1]}", columns.items()))}>'
