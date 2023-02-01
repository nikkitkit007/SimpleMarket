import asyncio

from server.cart.cart_obj import Cart
from data_base.tbl_workers.cart_tbl_worker import CartTblWorker
from data_base.tbl_workers.cart_list_tbl_worker import CartListTblWorker
from data_base.connection import get_session


class CartWorker(Cart):

    @staticmethod
    async def add_product_to_cart(product_id: int, cart_id: int):
        """
        1) добавляем продукт в таблицу CartList
        2) обновляем значения в таблице Cart в соответствии с ценой товара(price) и его количеством(1)
        """
        local_session = await get_session()
        async with local_session() as session:
            await CartListTblWorker.add(cart_id=cart_id,
                                        product_id=product_id,
                                        local_session=session)
            await CartTblWorker.update_cart(cart_id=cart_id,
                                            product_id=product_id,
                                            local_session=session)
            await session.commit()

    @staticmethod
    async def upd_product_count(product_id: int, cart_id: int, count: int) -> bool:
        local_session = await get_session()
        if count == 0:
            return True

        async with local_session() as session:
            product_count_in_cart = await CartListTblWorker.get_product_count_in_cart(cart_id=cart_id,
                                                                                      product_id=product_id,
                                                                                      local_session=session)
            if int(product_count_in_cart) + count > 0:
                await CartListTblWorker.update_product_count(cart_id=cart_id,
                                                             product_id=product_id,
                                                             count=count,
                                                             local_session=session)
            elif int(product_count_in_cart) + count == 0:
                await CartListTblWorker.delete_product_from_cart(cart_id=cart_id,
                                                                 product_id=product_id,
                                                                 local_session=session)
            else:
                return False        # new error

            await CartTblWorker.update_cart(cart_id=cart_id,
                                            product_id=product_id,
                                            count=count,
                                            local_session=session)
            await session.commit()

    @staticmethod
    async def get(cart_id: int):
        return None


async def create_test_cart():
    local_session = await get_session()
    async with local_session() as session:
        await CartTblWorker.add(1, session)
        await session.commit()


if __name__ == "__main__":
    asyncio.run(create_test_cart())
