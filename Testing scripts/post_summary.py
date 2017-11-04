from flask import Flask, request, jsonify
from bme590hrmfixed.get_ecg3 import Ecg
import json
from csvtojson import csvtojson
app = Flask(__name__)


def send_error(message, code):
    err = {
        "error": message
    }
    return jsonify(err), code


@app.route("/api/heart_rate/summary", methods=['POST'])
def summary():
    # data = request.json
    data_raw = request.files['']
    data = csvtojson(data_raw)

    try:
        isinstance(data, dict) is True
    except TypeError:
        # 400 refers to bad request
        return send_error("The input is not in dict format", 400)

    try:
        len(data["time"]) > 0 and len(data["voltage"]) > 0
    except ValueError:
        # 400 refers to bad request
        return send_error("The input is empty ", 400)

    data = Ecg(data, update_time=5,
               brady_threshold=60, tachy_threshold=100, user_sec=10, status=0)
    data.prep_data()
    data.get_max_peak()
    data.get_inst_hr()
    data.get_avghr()
    data.get_bradtach()
    data.summary()
    return_summary = data.ecg_summary
    return jsonify(return_summary)
