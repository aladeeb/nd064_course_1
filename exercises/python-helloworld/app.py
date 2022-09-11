from flask import Flask
from flask import Response
from flask import json

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World, Ahmed!"

@app.route("/metrics")
def metrics():
    return Response(json.dumps({"UserCount": 140, "UserCountActive": 23}), status=200, mimetype='application/json')

@app.route("/status")
def status():
    return Response("result: OK - healthy", status=200, mimetype='application/json')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000)
