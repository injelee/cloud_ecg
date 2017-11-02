from flask import Flask,jsonify, request
import numpy as np 
import math
from multiprocessing import Value

counter = Value('i',0)
app = Flask(__name__)


@app.route("/api/requests")
@app.before_request
def inc_count():
    counter.value += 1
    count = counter.value
    return jsonify("Number of views {}".format(count))
