from typing import Tuple
import flask
from flask import request, jsonify
from starlette import status

from server import logger
from server.cart.cart_worker import CartWorker


class CartHandler:

    @staticmethod
    async def add_product() -> Tuple[flask.Response, int]:
        data = request.json
        product_id = int(data["product_id"])
        cart_id = int(data["cart_id"])

        success_resp = {"Result": "Product added"}
        no_success_resp = {"Result": "Product not added"}

        try:
            await CartWorker.add_product_to_cart(product_id=product_id,
                                                 cart_id=cart_id)

            logger.info(f"Product with id {product_id} added in cart with id {cart_id}")
            return jsonify(success_resp), status.HTTP_200_OK
        except Exception as E:
            logger.error(E)
            return jsonify(no_success_resp), status.HTTP_400_BAD_REQUEST

    @staticmethod
    async def upd_product_count() -> Tuple[flask.Response, int]:
        data = request.json
        product_id = int(data.get("product_id"))
        cart_id = int(data.get("cart_id"))
        count = int(data.get("count"))

        success_resp = {"Result": "Successfully changed count of products in cart"}
        no_success_resp = {"Result": "Count of products in cart not changed"}

        try:
            await CartWorker.upd_product_count(product_id=product_id,
                                               cart_id=cart_id,
                                               count=count)
            logger.info(f"Count product with id {product_id} changed on "
                        f"{count} in cart with id {cart_id}")

            return jsonify(success_resp), status.HTTP_200_OK
        except Exception as E:
            logger.error(E)
            return jsonify(no_success_resp), status.HTTP_400_BAD_REQUEST

