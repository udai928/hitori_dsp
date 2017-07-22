# -*-coding:utf-8-*-
import MySQLdb
from resources import config

SELECT_ASTR_ACTIVE_CREATIVE_UPDATE_DESC = u"select * from creative where soft_delete_flag = 'open' order by update_time desc limit 5;"
INSERT_INTO_CREATIVE = u"insert into creative (creative_name,width,height,image_url,descriptions,create_time) values (%s,%s,%s,%s,%s,now());"

def select_all_creative_table():
    connection = MySQLdb.connect(
        host=config.HOST, user=config.USER, port=config.PORT, passwd=config.PASSWORD, db=config.DB, charset='utf8')
    cursor = connection.cursor()
    sql = SELECT_ASTR_ACTIVE_CREATIVE_UPDATE_DESC
    cursor.execute(sql)
    results = cursor.fetchall()
    cursor.close()
    connection.close()
    return results


def insert_creative(creative_to_insert):
    connection = MySQLdb.connect(
        host=config.HOST, user=config.USER, port=config.PORT, passwd=config.PASSWORD, db=config.DB, charset='utf8')
    cursor = connection.cursor()
    sql = INSERT_INTO_CREATIVE
    creative_name = creative_to_insert.get_creative_name()
    creative_width = int(creative_to_insert.get_width())
    creative_height = int(creative_to_insert.get_height())
    creative_image_url = creative_to_insert.get_image_url()
    creative_descriptions = creative_to_insert.get_descriptions()
    cursor.execute(sql, (creative_name, creative_width, creative_height, creative_image_url, creative_descriptions))
    connection.commit()
    cursor.close()
    connection.close()
