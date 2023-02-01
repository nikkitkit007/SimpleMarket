
from typing import Tuple
import flask
from starlette import status

from sqlalchemy import select

from data_base.connection import get_session


class HealthHandler:

    @staticmethod
    async def app() -> Tuple[flask.Response, int]:

        return flask.make_response("App live"), status.HTTP_200_OK

    @staticmethod
    async def db():
        local_session = await get_session()
        async with local_session() as session:
            query = select(1)
            result = await session.execute(query)
        if result:
            return flask.make_response("DB live"), status.HTTP_200_OK
        else:
            return flask.make_response("DB not connected"), status.HTTP_500_INTERNAL_SERVER_ERROR
