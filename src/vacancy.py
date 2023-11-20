import json


class Vacancy:
    def __init__(self, title, link, description, salary):
        self.title = title
        self.link = link
        self.description = description
        self.salary = salary

    def __repr__(self):
        return (f'Вакансии: {self.title} \n'
                f'Сайт: {self.link} \n'
                f'Описание: {self.description} \n'
                f'Зарплата: {self.salary}')


with open('../cache_json/cache_hh.json', 'r') as file:
    vacancy = json.load(file)
    vacancy_s = []
    for i in vacancy:
        vacancy_s.append(Vacancy(i['profession'], i['link'], i['candidat'], i['payment_from']))
for vacancy in vacancy_s:
    print(vacancy)


