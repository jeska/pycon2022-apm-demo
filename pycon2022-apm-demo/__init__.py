import logging
import os

from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

app = Flask(__name__)
app.config["ELASTIC_APM"] = {
    "SERVICE_NAME": "pycon2022-apm-demo",
    "SECRET_TOKEN": os.environ.get("APM_SECRET_TOKEN"),
    "SERVER_URL": os.environ.get("APM_SERVICE_URL"),
    "ENVIRONMENT": "demo",
}
apm = ElasticAPM(app, logging=logging.DEBUG)


@app.route("/")
def hello_pycon():
    return "Hello, Pycon!"


@app.route("/logger")
def hello_logger():
    try:
        1 / 0
    except ZeroDivisionError:
        app.logger.error("This is a pycon error", exc_info=True)
    finally:
        return "We've logged an error!"


@app.errorhandler(404)
def page_not_found(error):
    app.logger.error(f"This page doesn't exist, Pycon: {error}", exc_info=True)
    return "Page not found, try again."
