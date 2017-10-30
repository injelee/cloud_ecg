from flask import Flask,request

def test_response_count():
    FLASK_APP = ecg_api.py  flask  run  --host  0.0.0.0
    url = 'http://vcm-1849.vm.duke.edu:5000/'  #change to final server
    for i in range(10):
        request.get(url)
    assert g.count == 10

        
