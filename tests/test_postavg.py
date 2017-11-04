"""
Creating test class for average HR and brady/tachycardia data

"""

import unittest
from bme590hrmfixed.get_ecg3 import Ecg
from tests.csvtojson_post import csvtojson_post


class test_averagehr(unittest.TestCase):

    def test_output(self):
        data = csvtojson_post('test_data9_3.csv')
        ecg_data = Ecg(data, update_time=5,
                       brady_threshold=60, tachy_threshold=100,
                       user_sec=5, status=1)
        ecg_data.prep_data()
        ecg_data.get_max_peak()
        ecg_data.get_inst_hr()
        ecg_data.get_avghr()
        ecg_data.as_dict()
        assert isinstance(ecg_data.ecg_dict, dict) is True

    def test_output_value(self):
        data = csvtojson('test_data9_3.csv')
        ecg_data = Ecg(data, update_time=5,
                       brady_threshold=60, tachy_threshold=100,
                       user_sec=5, status=1)
        ecg_data.prep_data()
        ecg_data.get_max_peak()
        ecg_data.get_inst_hr()
        ecg_data.get_avghr()
        ecg_data.as_dict()
        # create sample data for this case
        assert ecg_data.avg_hr == [72.0, 60.673333333333332,
                                   82.959999999999994,
                                   93.36666666666666, 104.2]

    def test_output_lengths(self):
        # create sample data for this case
        data = csvtojson('test_data9_3.csv')
        ecg_data = Ecg(data, update_time=5,
                       brady_threshold=60, tachy_threshold=100,
                       user_sec=5, status=1)
        ecg_data.prep_data()
        ecg_data.get_max_peak()
        ecg_data.get_inst_hr()
        ecg_data.get_avghr()
        ecg_data.get_bradtach()
        ecg_data.as_dict()
        assert len(ecg_data.brady) == len(ecg_data.tachy) == 5

