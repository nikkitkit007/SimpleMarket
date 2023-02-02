import asyncio

from server.cart.cart_worker import create_test_cart


if __name__ == "__main__":
    cart_id = [1, 2]
    for _id in cart_id:
        asyncio.run(create_test_cart(_id))
