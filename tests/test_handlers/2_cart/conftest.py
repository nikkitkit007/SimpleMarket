import pytest

from server.cart.cart_obj import Cart


@pytest.fixture
def get_one_cart() -> dict:
    cart = Cart()

    cart.cart_id = 1
    cart.total_price = 100
    cart.products_count = 1
    cart.product_id = 1

    return cart.__dict__
