from flask import Flask
from flask import render_template
from interfaceFrameWork import 


app = Flask(__name__)

@app.route('/')
def index():
    greeting = "Hello World"
    return render_template("index.html", greeting=greeting)
    # return greeting

if __name__ == "__main__":
    app.run()
