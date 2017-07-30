# -*-coding:utf-8-*-

from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('post_json.html')


@app.route('/post', methods=['POST'])
def post():
    print(request.headers['Content-Type'])
    return jsonify(request.json)


if __name__ == "__main__":
    app.run("0.0.0.0")
    app.debug()
