import dotenv
import requests

from config import URL_SJ
from src.data_json.work_with_json import WorkWithJson

config = dotenv.dotenv_values(".env")


class RequestsSJ(WorkWithJson):
    """Класс, который отправляет запрос на сайт по поиску работы SuperJob"""

    def __init__(self, keyword, page=1) -> None:
        self.url = URL_SJ
        self.params = {"keywords": keyword, "page": page}

    def request(self) -> dict:
        """Метод класса, который обращается на сайт SJ по ключу и возвращает
        файл в формате json с данными о вакансиях"""
        headers = {
            "X-Api-App-Id": "v3.r.112492319.a7c4a3d27213114ba6c67347ae3a6264084122a7.19153f63812efb61654ff50fcdf7d91e1c1c7cfb"
        }
        responce = requests.get(self.url, params=self.params, headers=headers)
        return WorkWithJson.save_json(responce.json()["objects"])
