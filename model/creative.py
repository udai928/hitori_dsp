# -*-coding:utf-8-*-

class Creative:

    def __init__(self,creative_name,width,height,image_url,descriptions):
        self.creative_name = creative_name
        self.width = width
        self.height = height
        self.image_url = image_url
        self.descriptions = descriptions

    def get_creative_name(self):
        return self.creative_name

    def set_creative_name(self,creative_name):
        self.creative_name = creative_name

    def get_width(self):
        return self.width

    def set_width(self,width):
        self.width = width

    def get_height(self):
        return self.height

    def set_height(self,height):
        self.height = height

    def get_image_url(self):
        return self.image_url

    def set_image_url(self,image_url):
        self.image_url = image_url

    def get_descriptions(self):
        return self.descriptions

    def set_descriptions(self,descriptions):
        self.descriptions = descriptions