from flask import Flask,request
from ecg_api import inc_count


def test_response_count():
    url = 'http://vcm-1849.vm.duke.edu:5000/'  #change to final server
    for i in range(10):
        request.get(url)
    c = inc_count()
    assert c == 10

        
