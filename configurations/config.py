import os
from dotenv import load_dotenv
from os import environ

from pydantic import BaseSettings

dotenv_path = os.path.join(os.path.dirname(__file__), '../.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


class DefaultSettings(BaseSettings):
    """
    Default configs for application.
    """

    APP_HOST: str = environ.get("APP_HOST", "127.0.0.1")
    APP_PORT: int = int(environ.get("APP_PORT", 8080))

    POSTGRES_DB: str = environ.get("POSTGRES_DB", "postgres")
    POSTGRES_HOST: str = environ.get("POSTGRES_HOST", "localhost")
    POSTGRES_USER: str = environ.get("POSTGRES_USER", "user")
    POSTGRES_PORT: int = int(environ.get("POSTGRES_PORT", "5432"))
    POSTGRES_PASSWORD: str = environ.get("POSTGRES_PASSWORD", "mysecretpassword")

    PATH_PREFIX: str = environ.get("PATH_PREFIX", "")  # api/v1

    @property
    def database_settings(self) -> dict:
        """
        Get all DefaultSettings for connection with database.
        """
        return {
            "database": self.POSTGRES_DB,
            "user": self.POSTGRES_USER,
            "password": self.POSTGRES_PASSWORD,
            "host": self.POSTGRES_HOST,
            "port": self.POSTGRES_PORT,
        }

    @property
    def database_uri(self) -> str:
        """
        Get uri for connection with database.
        """
        return "postgresql+asyncpg://{user}:{password}@{host}:{port}/{database}".format(
            **self.database_settings,
        )

    @property
    def host_address(self):
        return f"http://{self.APP_HOST}:{self.APP_PORT}"
