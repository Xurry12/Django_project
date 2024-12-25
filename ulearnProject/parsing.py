from bs4 import BeautifulSoup
import requests
from datetime import datetime, timedelta

def clean_html(html_text):
    soup = BeautifulSoup(html_text, 'html.parser')
    return soup.get_text()

def get_salary(salary):
  if salary is None:
    return "Доход не указан"
  else:
    if salary['from'] is None and salary['to'] is not None:
      return f"До {salary['to']} {salary['currency']}."
    elif salary['from'] is not None and salary['to'] is None:
      return f"От {salary['from']} {salary['currency']}."
    else:
      return f"От {salary['from']} до {salary['to']} {salary['currency']}"


def get_skills(skills):
  if len(skills) == 0 or skills is None:
    return "Навыки не указаны"
  else:
    res = []
    for skill in skills:
      res.append(skill['name'])
    return ", ".join(res)


result = {}


def get_vacancies(profession):
    params = {
        'text': profession,
        'period': 1,
        'per_page': 10,
        "search_field": 'name',
        'page': 0,
        'order_by': 'publication_time'
    }

    response = requests.get('https://api.hh.ru/vacancies', params=params)

    if response.status_code != 200:
        print(f"Ошибка при запросе: {response.status_code}")
        return []

    vacancies = response.json().get('items', [])
    results = []

    for vacancy in vacancies:
        vacancy_data = {
            'id': vacancy['id'],
            'title': vacancy['name'],
            'company': vacancy['employer']['name'],
            'salary_info': get_salary(vacancy['salary']),
            'region': vacancy['area']['name'],
            'published_at': vacancy['published_at'],
            'description': '',
            'skills': ''
        }

        vacancy_details = requests.get(vacancy['url'])
        if vacancy_details.status_code == 200:
            details = vacancy_details.json()
            vacancy_data['description'] = clean_html(details.get('description', 'Нет описания'))
            vacancy_data['skills'] = get_skills(details.get('key_skills', 'Нет навыков'))

        results.append(vacancy_data)
        result[vacancy['id']] = vacancy_data
    return results


profession_variants = ['analytic', 'аналитик', 'analyst', 'аналітик', 'Аналитик']

for profession in profession_variants:
    get_vacancies(profession)

# for vac in result.values():
#     print(f"Название: {vac['title']}")
#     print(f"Описание: {vac['description']}")
#     print(f"Навыки: {vac['skills']}")
#     print(f"Компания: {vac['company']}")
#     print(f"Оклад: {vac['salary_info']}")
#     print(f"Регион: {vac['region']}")
#     print(f"Дата публикации: {vac['published_at']}")
#     print("-" * 40)