# -*-coding:utf-8-*-

from flask import Flask, render_template, request, jsonify, json
import json

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('post_json.html')


@app.route('/post', methods=['POST'])
def post():

    print(request.headers['Content-Type'])

    request_obj = json.loads(request.json)

    #リクエスト情報に適う配信可能ストラクトを取得する。
    print(request_obj['site']['cat'])
    #配信可能ストラクトで内部オークションする。

    #入札対象ストラクトでレスポンスを生成する。




    #return jsonify(response.json)
    return jsonify(request.json)


if __name__ == "__main__":
    app.run("0.0.0.0")
    app.debug()
