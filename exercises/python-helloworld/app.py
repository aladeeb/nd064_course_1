from flask import Flask
from flask import Response
from flask import json
import logging

logging.basicConfig(filename="app.log", level="DEBUG")

app = Flask(__name__)

@app.route("/")
def hello():
    logging.debug("Hello World")
    return "Hello World, Ahmed!"

@app.route("/metrics")
def metrics():
    logging.info("This is a metrics request")
    return Response(json.dumps({"UserCount": 140, "UserCountActive": 23}), status=200, mimetype='application/json')

@app.route("/status")
def status():
    logging.debug("Someone hit the status API")
    return Response("result: OK - healthy", status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
