import pytest

from server.product.product_obj import Product


@pytest.fixture
def get_one_product() -> dict:
    test_product = Product()
    test_product.id = 1
    test_product.name = "test_product"
    test_product.manufacturer = "test_manufacturer"
    test_product.price = 12345678

    return test_product.__dict__
