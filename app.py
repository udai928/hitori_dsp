# -*-coding:utf-8-*-

from flask import Flask, render_template, request
from service import creative_service

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html', message="Hello World! Hello Flask!")


@app.route('/select')
def show_creatives():
    creative_info_list = creative_service.get_creative_info_list()
    return render_template('index.html', creative_list=creative_info_list)


@app.route('/form')
def show_form():
    return render_template('form.html')


@app.route('/result', methods=['POST', 'GET'])
def result():
    if request.method == 'POST':
        creative_service.creative_register(request.form)
        creative_info_list = creative_service.get_creative_info_list()
        return render_template('index.html', creative_list=creative_info_list)


if __name__ == "__main__":
    app.run("0.0.0.0")
    app.debug()
