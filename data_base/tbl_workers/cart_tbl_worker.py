from sqlalchemy import select, insert, update, and_

from data_base.models.cart_model import Cart
from data_base.tbl_workers.product_tbl_worker import ProductTblWorker


class CartTblWorker(Cart):

    @staticmethod
    async def add(cart_id, local_session):

        cart_obj = {"id": cart_id}
        add_product_query = insert(Cart).values(
            cart_obj
        )
        await local_session.execute(add_product_query)

    @staticmethod
    async def get(local_session) -> list:
        """

        """
        query = select(Cart)

        result = await local_session.execute(query)
        products = result.scalars().all()

        return products

    @staticmethod
    async def update_cart(cart_id: int, product_id: int, count: int, local_session):
        """
        Обновляем значения count и price таблицы Cart.
        Значения берем из таблицы CartList
        """
        product = await ProductTblWorker.get_by_id(product_id=product_id, local_session=local_session)

        if product:
            prod_price = product.price

            data_to_update = dict(price=Cart.price+prod_price*count, count=Cart.count+count)

            query = update(Cart).\
                where(and_(Cart.id == cart_id)).\
                values(data_to_update)

            await local_session.execute(query)
