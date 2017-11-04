from flask import Flask,jsonify,request
import numpy as np 
import math
from bme590hrmfixed.get_ecg3 import Ecg
from csvtojson import csvtojson
from multiprocessing import Value

app = Flask(__name__)
counter = Value('i',0)

def send_error(message, code):
    err = {
        "error": message
    }
    return jsonify(err), code

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

  
@app.route("/api/heart_rate/average/", methods=["Post"])
def jsonavg():
    """
    This module takes in JSON inputs and uses a previously created class to
    determine average heart rate over an averaging window, as well
    as outputting brady/tachycardia arrays on the avghr data.

    :return:
    """

    data1 = request.files['']
    data = csvtojson(data1)
    # data = request.json
    try:
        isinstance(data, dict) is True
    except TypeError:
        return send_error("Input was not of type=dictionary.", 400)

    try:
        len(data) is 3
    except TypeError:
        return send_error("Input dict did not have length 3 (either too small"
                          " or too large). Please "
                          "input dictionary with 3 keys.", 431)

    avg_period = data["averaging_period"]

    try:
        isinstance(avg_period, float) is True
    except ValueError:
        return send_error("Averaging_period used could not be taken "
                          "from the dictionary as type=float,"
                          "or was not initially type float (e.g. str).", 400)

    ecg_data = Ecg(data, update_time=5, brady_threshold=60,
                   tachy_threshold=100, user_sec=avg_period, status=1)
    ecg_data.prep_data()
    ecg_data.get_max_peak()
    ecg_data.get_inst_hr()
    ecg_data.get_avghr()
    ecg_data.get_bradtach()
    ecg_data.as_dict()

    json_dict = ecg_data.ecg_dict

    try:
        isinstance(json_dict, dict) is True
    except TypeError:
        return send_error("Initial data could not be "
                          "converted to type=dict.", 500)

    return jsonify(json_dict)
