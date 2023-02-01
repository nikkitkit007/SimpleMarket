import requests
from starlette import status


class TestProduct:
    def test_add(self, base_url, get_one_product):
        api = "/product"
        product = get_one_product

        response = requests.post(base_url + api, json=product)

        assert response.status_code == status.HTTP_200_OK

    def test_get(self, base_url):
        api = "/product"
        price_min = 0
        price_max = 10000
        sorting = "name_down"
        params = {"price_min": price_min,
                  "price_max": price_max,
                  "sorting": sorting}
        response = requests.get(base_url + api, params=params)

        assert response.status_code == status.HTTP_200_OK
