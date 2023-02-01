
from server.product.product_obj import Product
from data_base.tbl_workers.product_tbl_worker import ProductTblWorker
from data_base.connection import get_session


class ProductWorker(Product):

    @staticmethod
    async def add_to_storage(product: dict):
        local_session = await get_session()
        async with local_session() as session:
            await ProductTblWorker.add(product, session)
            await session.commit()

    @staticmethod
    async def get(price_min: int = None, price_max: int = None, sorting: str = None) -> dict:

        local_session = await get_session()
        async with local_session() as session:
            products = await ProductTblWorker.get_all(session, price_min, price_max, sorting)
            await session.commit()

        all_products = {}

        for product in products:
            key_val = str(product.id)
            adding_parth = product.to_dict(exclude_keys=["id"])

            all_products[key_val] = adding_parth

        return all_products
