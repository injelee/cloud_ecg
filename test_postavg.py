"""
Creating test class for average HR and brady/tachycardia data

"""

import unittest
from get_ecg import Ecg


class test_average_hr(unittest.TestCase):

    def test_output(self):
        data = Ecg(csv_file='/Users/injelee/cloud_ecg/test_data/test_data9.csv', update_time=5,
                   brady_threshold=60, tachy_threshold=100, user_sec=5)
        data.prep_data()
        data.get_max_peak()
        data.get_inst_hr()
        data.get_avghr()
        data.as_dict()
        assert isinstance(data.ecg_dict, dict) is True

    def test_output_value(self):
        data = Ecg(csv_file='/Users/injelee/cloud_ecg/test_data/test_data9.csv', update_time=5,
                   brady_threshold=60, tachy_threshold=100, user_sec=5)
        data.prep_data()
        data.get_max_peak()
        data.get_inst_hr()
        data.get_avghr()
        data.as_dict()
        # create sample data for this case
        assert data.avg_hr == [72.0, 60.673333333333332, 82.959999999999994, 93.36666666666666, 104.2]

    def test_output_lengths(self):
        # create sample data for this case
        data = Ecg(csv_file='/Users/injelee/cloud_ecg/test_data/test_data9.csv', update_time=5,
                   brady_threshold=60, tachy_threshold=100, user_sec=5)
        data.prep_data()
        data.get_max_peak()
        data.get_inst_hr()
        data.get_avghr()
        data.as_dict()
        assert len(data.brady) == len(data.tachy) == len(data.raw_bunches) == 10000

