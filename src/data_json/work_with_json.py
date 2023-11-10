import json

from config import JSON_HH


class WorkWithJson:
    path = JSON_HH

    @classmethod
    def save_json(cls, data):
        with open(cls.path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=4)


