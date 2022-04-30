# pycon2022-apm-demo

To run, install `poetry` and run the following:

```bash
poetry run flask run
 * Serving Flask app 'pycon2022-apm-demo' (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 ```
 
 You will also need an Elastic cluster with APM enabled. You can do this on [Elastic Cloud](https://cloud.elastic.co) and follow the instructions under the APM Integration for Flask. Export your APM Secret Token & Service URL as the environment variables `APM_SECRET_TOKEN` and `APM_SERVICE_URL` respectively.
