# -*-coding:utf-8-*-

from model import creative as model_creative
from dao import creative_dao
from PIL import Image
from urllib.request import urlopen
import io

def get_creative_info_list():
    creative_info_list = []
    results = creative_dao.select_all_creative_table()
    for result in results:
        creative = model_creative.Creative(result[1], result[2], result[3], result[4], result[5])
        creative_info = {}
        creative_info['creative_name'] = creative.get_creative_name()
        creative_info['width'] = creative.get_width()
        creative_info['height'] = creative.get_height()
        creative_info['img_url'] = creative.get_image_url()
        creative_info_list.append(creative_info)

    return creative_info_list


def creative_register(request_form):
    image_url = request_form['image_url']
    file = io.BytesIO(urlopen(image_url).read())
    img = Image.open(file)
    creative_to_insert = model_creative.Creative(request_form['creative_name'], img.size[0], img.size[1], image_url, request_form['descriptions'])
    creative_dao.insert_creative(creative_to_insert)
