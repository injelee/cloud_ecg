"""
Creating test class for average HR and brady/tachycardia data

"""

import unittest
import get_ecg


class testavghr(unittest.TestCase):
    data = get_ecg(json_file=filename, update_time=5,
                     brady_threshold=60, tachy_threshold=100, mins=2)
    data.prep_data()
    data.get_max_peak()
    data.get_inst_hr()
    data.get_avghr()

    def test_output(self):
        if isinstance(self.realbunches, list) is True:
            test = 1
        assert test == 1

    def test_output_value(self):
        # create sample data for this case

    def test_output_error(self):
        # create sample data for this case


