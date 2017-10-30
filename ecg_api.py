from flask import Flask,jsonify, request
import numpy as np 
import math
from multiprocessing import Value

counter = Value('i', 0)
app = Flask(__name__)


@app.before_request()
def before_request():
    with counter.get_lock():
        counter.value += 1
        g.count = counter.value


@app.route("/api/requests")
def request_count():
    return "Number of views {}".format(g.count)
