import os

from elasticapm.contrib.flask import ElasticAPM
from flask import Flask

app = Flask(__name__)
app.config['ELASTIC_APM'] = {
    'SERVICE_NAME': 'pycon2022-apm-demo',
    'SECRET_TOKEN': os.environ.get("APM_SECRET_TOKEN"),
    'SERVER_URL': os.environ.get("APM_SERVICE_URL"),
    'ENVIRONMENT': 'demo',
}
apm = ElasticAPM(app)


@app.route('/')
def hello_pycon():
    return 'Hello, Pycon!'
