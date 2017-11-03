from flask import Flask, request, jsonify
from bme590hrmfixed.get_ecg3 import Ecg
import json
app = Flask(__name__)


def send_error(message, code):
    err = {
        "error": message
    }
    return jsonify(err), code


@app.route("api/heart_rate/summary", methods=['POST'])
def summary():
    if request.method == 'POST':
        data = request.json

    try:
        isinstance(data, dict) is True
    except TypeError:
        return send_error("The input is not in dict format", 400)  # 400 refers to bad request

    try:
        len(data['time']) != 0 and len(data['voltage']) != 0
    except ValueError:
        return send_error("The input is empty ", 400)  # 400 refers to bad request

    data = Ecg(data, update_time=5,
               brady_threshold=60, tachy_threshold=100, mins=2)
    data.prep_data()
    data.get_max_peak()
    data.get_inst_hr()
    data.get_avghr()
    return_summary = data.ecg_summary()
    return jsonify(return_summary)








