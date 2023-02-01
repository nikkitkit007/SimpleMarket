from server.__main__ import app
from configurations.config import DefaultSettings


if __name__ == '__main__':
    host = DefaultSettings().APP_HOST
    port = DefaultSettings().APP_PORT
    app.run(host=host,
            port=port)
