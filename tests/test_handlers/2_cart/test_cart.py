import requests
from starlette import status


class TestCart:
    def test_add_product(self, base_url):
        api = "/cart"
        add_product = {"product_id": 2,
                       "cart_id": 1}

        response = requests.post(base_url + api, json=add_product)

        assert response.status_code == status.HTTP_200_OK

    def test_upd_product_count(self, base_url):
        api = "/cart"

        product_id = 1
        cart_id = 1
        count = -10
        upd_params = {"product_id": product_id,
                      "cart_id": cart_id,
                      "count": count}

        response = requests.put(base_url + api, json=upd_params)

        assert response.status_code == status.HTTP_200_OK
