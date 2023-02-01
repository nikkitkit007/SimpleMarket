
from typing import Tuple
import flask
from flask import request, jsonify
from starlette import status

from server.product.product_worker import ProductWorker


class ProductHandler:

    @staticmethod
    async def add() -> Tuple[flask.Response, int]:
        data = request.json

        await ProductWorker.add_to_storage(data)
        return flask.make_response("Product added"), status.HTTP_200_OK

    @staticmethod
    async def get():
        data = request.args
        price_min = data.get("price_min")
        price_max = data.get("price_max", None)
        sorting = data.get("sorting", None)
        products = await ProductWorker.get(price_min=price_min,
                                           price_max=price_max,
                                           sorting=sorting)

        return jsonify(products), status.HTTP_200_OK

    @staticmethod
    async def delete() -> Tuple[flask.Response, int]:

        return flask.make_response("Product deleted"), 200
