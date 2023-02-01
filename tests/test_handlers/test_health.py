
import requests
from starlette import status


class TestHealth:
    def test_ping_app(self, base_url):
        method = "/health/app"
        response = requests.get(base_url + method)

        assert response.status_code == status.HTTP_200_OK

    def test_ping_db(self, base_url):
        method = "/health/db"
        response = requests.get(base_url + method)

        assert response.status_code == status.HTTP_200_OK


