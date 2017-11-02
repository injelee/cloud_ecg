from flask import Flask,jsonify, request
import numpy as np 
import math
from get_ecg.py import Ecg

app = Flask(__name__)


@app.route("/api/heart_rate/average/", methods=["Post"])
def jsonavg():
    """
    This module takes in JSON inputs and uses a previously created class to
    determine average heart rate over an averaging window, as well as outputting brady/
    tachycardia arrays on both inst. hr and avg. hr inputs.

    :return:
    """
    data = request.json
    user_sec = data.averaging_period
    time = data.time
    voltage = data.voltage
    ecg_data = Ecg(data, update_time=5, brady_threshold=60, tachy_threshold=100,
                   user_sec=20)
    ecg_data.prep_data()
    ecg_data.get_max_peak()
    ecg_data.get_inst_hr()
    ecg_data.get_avghr()
    ecg_data.as_dict()

    return jsonify(ecg_data.ecg_dict)



