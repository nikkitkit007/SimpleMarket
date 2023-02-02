from sqlalchemy import select, insert, and_, update, delete

from data_base.models.cart_list_model import CartList


class CartListTblWorker(CartList):

    @staticmethod
    async def add(cart_id: int, product_id: int, local_session):
        cart_list_obj = {"cart_id": cart_id, "product_id": product_id}
        add_product_query = insert(CartList).values(
            cart_list_obj
        )
        await local_session.execute(add_product_query)

    @staticmethod
    async def get_product_count_in_cart(cart_id: int, product_id: int, local_session) -> int:
        query = select(CartList.count).where(and_(CartList.cart_id == cart_id),
                                             and_(CartList.product_id == product_id)).limit(1)

        result = await local_session.execute(query)
        products_count = result.scalars().first()
        return products_count

    @staticmethod
    async def update_product_count(cart_id: int, product_id: int, count: int, local_session):
        try:
            data_to_update = dict(count=CartList.count + count)

            query = update(CartList). \
                where(and_(CartList.cart_id == cart_id),
                      and_(CartList.product_id == product_id)). \
                values(data_to_update)

            await local_session.execute(query)
        except:
            print("ERROR, record in cart list not found")

    @staticmethod
    async def delete_product_from_cart(cart_id: int, product_id: int, local_session):

        query = delete(CartList). \
            where(and_(CartList.cart_id == cart_id),
                  and_(CartList.product_id == product_id))

        await local_session.execute(query)
