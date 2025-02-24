# PythonFlaskPlayground

How to run the Flask Server to return Json:
1. open proj from visual Code
2. python -m pip install flask
3. python -m pip install flask-cors
4. mark server.py on left window
5. from top menu => run => run without debugger
6. url for get request: http://127.0.0.1:5000/audio


How to run the Flask Server to return Json From CMD:
python server.py
or
flask --app server run
or
python -m flask --app server run


This application uses CORS policy.
To use it, you need to install flask-cors:
> pip install flask-cors


To run the Flask Server over https with Self Signed Certificate:
1. Get a .crt file and a .key file and place them in your file system
2. Point to the location of these files in the 'context' variable in server.py file. 
