"""
Creating test class for average HR and brady/tachycardia data

"""

import unittest
from get_ecg.py import Ecg


class test_avg_hr(unittest.TestCase):

    def test_output(self):
        data = Ecg(csv_file=filename, update_time=5,
                   brady_threshold=60, tachy_threshold=100, mins=2)
        data.prep_data()
        data.get_max_peak()
        data.get_inst_hr()
        data.get_avghr()
        data.as_dict()
        if isinstance(data.ecg_dict(), list) is True:
            test = 1
        assert test == 1

    def test_output_value(self):
        # create sample data for this case

    def test_output_error(self):
        # create sample data for this case


