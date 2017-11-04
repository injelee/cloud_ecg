[![Build Status](https://travis-ci.org/injelee/cloud_ecg.svg?branch=master)](https://travis-ci.org/injelee/cloud_ecg)

# Heart Rate Monitor with Web Service
This project is desiging a well-tested web service that performs heart rate calculations including heart rate and brady/tachycardia from ECG data sets. It is implemented from a class-based heart rate monitor project, which can be checked through the link below:
https://github.com/jl3392/bme590hrm

Running method
===============
The main file to run is called "ecg_api.py", which will be deployed on a public facing Virtual Machine (VM) as it would be in industry, allowing service to process requests
from any internet connected client (e.g. cloud connected ECG device, iOS/Android applications,
Web applications, etc).
Access the VM with the following address:http://vcm-1848.vm.duke.edu:5000/


License
==============
We choose to use Apache License, Version 2.0 for our project's license. Because this license provides an express grant of patent rights
from contributors to users.

Documentation
==============
The latest documentation is automatically generated using Sphinx and we're working on getting an accessible link. Stay tuned for updates! 


Contributors
============
Jing-Rui Li (jl714@duke.edu)
Inje Lee (inje.lee@duke.edu)
Niranjana Shashikumar (niranjana.shashikumar@duke.edu)
