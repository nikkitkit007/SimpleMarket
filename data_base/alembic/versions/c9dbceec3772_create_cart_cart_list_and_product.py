"""create cart, cart_list and product

Revision ID: c9dbceec3772
Revises: 
Create Date: 2023-01-31 19:36:56.312612

"""
from sqlalchemy import Column, ForeignKey
from sqlalchemy.dialects.postgresql import (INTEGER, TIMESTAMP, BOOLEAN, VARCHAR, ARRAY)

from alembic import op

import data_base.table_config as config


# revision identifiers, used by Alembic.
revision = 'c9dbceec3772'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        config.TBL_PRODUCT,
        Column("id", INTEGER, primary_key=True),
        Column('name', VARCHAR(255), nullable=False),
        Column('manufacturer', VARCHAR(255), nullable=False),
        Column('price', INTEGER, nullable=False),
    )
    op.create_table(
        config.TBL_CART,
        Column('id', INTEGER, primary_key=True),
        Column('count', INTEGER, nullable=False, default=0),
        Column('price', INTEGER, nullable=False, default=0),
    )
    op.create_table(
        config.TBL_CARTLIST,
        Column('id', INTEGER, primary_key=True),
        Column('cart_id', INTEGER, ForeignKey(f"{config.TBL_CART}.id"), nullable=False),
        Column('product_id', INTEGER, ForeignKey(f"{config.TBL_PRODUCT}.id"), nullable=False),
        Column('count', INTEGER, nullable=False, default=1),
    )
    op.create_unique_constraint(None, table_name=config.TBL_CARTLIST, columns=['cart_id', 'product_id'])


def downgrade() -> None:
    op.drop_table(config.TBL_CARTLIST)
    op.drop_table(config.TBL_CART)
    op.drop_table(config.TBL_PRODUCT)
