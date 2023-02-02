from typing import Tuple

import flask
from flask import request, jsonify
from starlette import status

from server import logger
from server.product.product_worker import ProductWorker


class ProductHandler:

    @staticmethod
    async def add() -> Tuple[flask.Response, int]:
        success_resp = {"Result": "Product created"}
        no_success_resp = {"Result": "Product not created"}
        data = request.json

        try:
            await ProductWorker.add_to_storage(data)
            logger.info(f"Product with name {data['name']} created")
            return jsonify(success_resp), status.HTTP_200_OK
        except Exception as E:
            logger.error(E)
            return jsonify(no_success_resp), status.HTTP_400_BAD_REQUEST

    @staticmethod
    async def get():
        no_success_resp = {"Result": "Error with getting data"}

        data = request.args

        name = data.get("name", None)
        manufacturer = data.get("manufacturer", None)

        price_min = data.get("price_min", None)
        price_max = data.get("price_max", None)
        sorting = data.get("sorting", None)

        try:
            products = await ProductWorker.get(name=name,
                                               manufacturer=manufacturer,
                                               price_min=price_min,
                                               price_max=price_max,
                                               sorting=sorting)
            return jsonify(products), status.HTTP_200_OK
        except Exception as E:
            logger.error(E)
            return jsonify(no_success_resp), status.HTTP_404_NOT_FOUND

    @staticmethod
    async def delete() -> Tuple[flask.Response, int]:

        return flask.make_response("Product deleted"), 200
