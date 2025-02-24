from flask import Flask
from markupsafe import escape
#from flask_cors import CORS

app = Flask(__name__)
#CORS(app)

@app.route('/')
def hello_world():
    print("__name__ in server.py = " + __name__)
    return '<p>Hello World!</p>'


@app.route("/audio")
def audio_data():
    return {
        "Track Name":"The NightFly",
        "Author Name":"Doland Fagen",
        "Duration":"5:47"
    }


#Example to send parameter "name" at the url and to print it
#@app.route("/<name>")
#def hello(name):
#    return f"Hello, {escape(name)}!"



if __name__ == '__main__':
    # Use this option to run regular http server
    app.run()

    # Use this option to run https server using ad-hoc certiciate (this is a built-in Flask capability used for development)
    # (Flask will generate a self-signed certificate on the fly when ever you run the server)
    #app.run(ssl_context='adhoc') 

    # Use this option to run https with Self Signed Certificate
    #context = ('C:\Workspaces\Python\certsAndKeys\channelUI_dev.crt', 'C:\Workspaces\Python\certsAndKeys\channelUI_dev.key') #certificate and key files
    #app.run(ssl_context=context)
