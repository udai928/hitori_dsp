# -*-coding:utf-8-*-

from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', message="Hello World! Hello Flask!")

if __name__ == "__main__":
    app.run("0.0.0.0")
    app.debug()