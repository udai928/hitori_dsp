# -*-coding:utf8-*-

import configparser
import MySQLdb

CONFIG = configparser.ConfigParser()
CONFIG_FILE = '../resources/config.ini'

CONFIG.read(CONFIG_FILE)
EXEC_ENV = CONFIG['common']['env']

def preapre_sample_dataum():

    connection = MySQLdb.connect(
        host=CONFIG[EXEC_ENV]['mysql_host']
        , user=CONFIG[EXEC_ENV]['mysql_user']
        , port=int(CONFIG[EXEC_ENV]['mysql_port'])
        , passwd=CONFIG[EXEC_ENV]['mysql_pass']
        , db=CONFIG[EXEC_ENV]['mysql_db']
        , charset='utf8'
    )
    cursor = connection.cursor()
    print(CONFIG[EXEC_ENV]['mysql_prepare_queries'])
    # 複数のSQLをまとめて実行したい。
    cursor.execute(CONFIG[EXEC_ENV]['mysql_prepare_queries'])
    connection.commit()
    cursor.close()
    connection.close()

if __name__ == "__main__":
    preapre_sample_dataum()
