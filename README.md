# Heart Rate Monitor with Web Service
This project is desiging a well-tested web service that performs heart rate calculations including heart rate and brady/tachycardia from ECG data sets.

Running method
===============
The main file to run is called "ecg_api.py", which will be deployed on a public facing Virtual Machine (VM) as it would be in industry, allowing service to process requests
from any internet connected client (e.g. cloud connected ECG device, iOS/Android applications,
Web applications, etc).

During the running process, it will ask user's input of "user-specified time". It will be used to average the heart rate under 
the specified time range. 
Please be sure to convert the time input into minutes.
For example:
If user wants to put in time as 300 seconds, please convert it to 5 minutes.

License
==============
We choose to use Apache License, Version 2.0 for our project's license. Because this license provides an express grant of patent rights
from contributors to users.

Documentation
==============
The latest documentation is automatically generated using Sphinx and can be found through the link below:


Contributors
============
Jing-Rui Li (jl714@duke.edu)
Inje Lee (inje.lee@duke.edu)
Niranjana Shashikumar (niranjana.shashikumar@duke.edu)
