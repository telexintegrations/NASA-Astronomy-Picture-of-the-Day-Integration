""" 
wsgi.py

Application entry point in production
"""

from . import config
from .server import server as app

if __name__ == "__main__":
    if config.env == "prod":
        app.run(
            host=config.app_host,
            port=config.app_port,
        )