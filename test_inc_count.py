from flask import Flask,request
from ecg_api import inc_count
import flaskr
import unittest

class FlaskrTestCase(unittest.TestCase):
    def test_response_count():
    url = 'http://127.0.0.1:5000/api/'  #change to final server
    for i in range(10):
       self.app.get(url)
    c =app.inc_count()
    assert c == 10

        
