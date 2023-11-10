from config import URL_HH
from src.abstract_class_api import WorkWithAbstract
import requests


class RequestHH(WorkWithAbstract):
    def __init__(self, keyword, area=113):
        self.url = URL_HH
        self.keyword = keyword
        self.area = area
        self.parameter = {'text': self.keyword, 'area': self.area}


    def request(self):
        responce = requests.get(self.url, self.parameter)
        return responce.json()

