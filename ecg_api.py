from flask import Flask,jsonify, request
from multiprocessing import Value


counter = Value('i',0)
app = Flask(__name__)


@app.route("/api/requests")
@app.before_request
def inc_count():
    """
    Method that counts number of requests handled by the web service.
    :params: None
    :return: number of requests in json format
    """
    counter.value += 1
    count = counter.value
    return jsonify("Number of requests {}".format(count))
