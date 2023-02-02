
from aioflask import Flask
from starlette import status

from server.cart.cart_handler import CartHandler
from server.product.product_handler import ProductHandler
from server.health.health_handler import HealthHandler


from configurations.config import DefaultSettings


app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

conf = DefaultSettings()


@app.route(f'/{conf.PATH_PREFIX}')
def index():

    return "Hi", status.HTTP_200_OK


def api_add_url():
    # -------------------------------Server-Status--------------------------------
    app.add_url_rule(rule=f"/{conf.PATH_PREFIX}/health/app",
                     view_func=HealthHandler.app,
                     methods=["GET"])
    app.add_url_rule(rule=f"/{conf.PATH_PREFIX}/health/db",
                     view_func=HealthHandler.db,
                     methods=["GET"])

    # ----------------------------------Product-----------------------------------
    app.add_url_rule(rule=f"/{conf.PATH_PREFIX}/product",
                     view_func=ProductHandler.add,
                     methods=["POST"])
    app.add_url_rule(rule=f"/{conf.PATH_PREFIX}/product",
                     view_func=ProductHandler.get,
                     methods=["GET"])

    # ------------------------------------Cart--------------------=---------------
    app.add_url_rule(rule=f"/{conf.PATH_PREFIX}/cart",
                     view_func=CartHandler.add_product,
                     methods=["POST"])
    app.add_url_rule(rule=f"/{conf.PATH_PREFIX}/cart",
                     view_func=CartHandler.upd_product_count,
                     methods=["PUT"])


api_add_url()
