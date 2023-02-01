from typing import Tuple
import flask
from flask import request, jsonify
from starlette import status

from server.cart.cart_worker import CartWorker


class CartHandler:

    @staticmethod
    async def add_product() -> Tuple[flask.Response, int]:
        data = request.json
        product_id = int(data["product_id"])
        cart_id = int(data["cart_id"])

        await CartWorker.add_product_to_cart(product_id=product_id,
                                             cart_id=cart_id)

        success_resp = {"Result": "Product added"}
        return jsonify(success_resp), status.HTTP_200_OK

    @staticmethod
    async def upd_product_count() -> Tuple[flask.Response, int]:
        data = request.json
        product_id = int(data.get("product_id"))
        cart_id = int(data.get("cart_id"))
        count = int(data.get("count"))

        await CartWorker.upd_product_count(product_id=product_id,
                                           cart_id=cart_id,
                                           count=count)

        success_resp = {"Result": "Successfully changed count of products in cart"}
        return jsonify(success_resp), status.HTTP_200_OK

