# -*-coding:utf-8-*-

from flask import Flask
from flask import render_template
import MySQLdb
import config

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html', message="Hello World! Hello Flask!")


@app.route('/select')
def db_save():
    connection = MySQLdb.connect(
        host=config.HOST, user=config.USER, port=config.PORT, passwd=config.PASSWORD, db=config.DB, charset='utf8')
    cursor = connection.cursor()
    sql = u"select * from creative limit 5;"
    cursor.execute(sql)
    result = cursor.fetchall()
    cursor.close()
    connection.close()

    return render_template('index.html', message=result)



if __name__ == "__main__":
    app.run("0.0.0.0")
    app.debug()

