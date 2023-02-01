import pytest


from configurations.config import DefaultSettings

conf = DefaultSettings()


@pytest.fixture
def base_url():
    host_address = conf.host_address
    prefix = conf.PATH_PREFIX

    address = f"{host_address}/{prefix}"

    return address

