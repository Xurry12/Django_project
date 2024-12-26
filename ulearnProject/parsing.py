import aiohttp
import asyncio
from bs4 import BeautifulSoup
from itertools import islice


result = {}

async def fetch(session, url, params=None):
    async with session.get(url, params=params) as response:
        if response.status != 200:
            print(f"Ошибка при запросе: {response.status}")
            return None
        return await response.json()


async def get_salary(salary):
    if salary is None:
        return "Доход не указан"
    else:
        if salary['from'] is None and salary['to'] is not None:
            return f"До {salary['to']} {salary['currency']}."
        elif salary['from'] is not None and salary['to'] is None:
            return f"От {salary['from']} {salary['currency']}."
        else:
            return f"От {salary['from']} до {salary['to']} {salary['currency']}"


def clean_html(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')
    return soup.get_text()


def get_skills(skills):
    if not skills:
        return 'Навыки не указаны'
    return ', '.join(skill['name'] for skill in skills)


async def get_vacancy_details(session, vacancy_url):
    details = await fetch(session, vacancy_url)
    if details:
        return {
            'description': clean_html(details.get('description', 'Нет описания')),
            'skills': get_skills(details.get('key_skills', []))
        }
    return {'description': '', 'skills': ''}


async def get_vacancies(profession):
    params = {
        'text': profession,
        'period': 1,
        'per_page': 10,
        "search_field": 'name',
        'page': 0,
        'order_by': 'publication_time'
    }

    async with aiohttp.ClientSession() as session:
        vacancies = await fetch(session, 'https://api.hh.ru/vacancies', params=params)

        if not vacancies:
            return []

        tasks = []
        for vacancy in vacancies.get('items', []):
            vacancy_data = {
                'id': vacancy['id'],
                'title': vacancy['name'],
                'company': vacancy['employer']['name'],
                'salary_info': await get_salary(vacancy['salary']),
                'region': vacancy['area']['name'],
                'published_at': vacancy['published_at'],
                'description': '',
                'skills': ''
            }
            if len(result) != 10:
                tasks.append(get_vacancy_details(session, vacancy['url']))
                result[vacancy['id']] = vacancy_data

        details_list = await asyncio.gather(*tasks)

        for i, details in enumerate(details_list):
            vacancy_id = vacancies['items'][i]['id']
            result[vacancy_id]['description'] = details['description']
            result[vacancy_id]['skills'] = details['skills']

        return result


async def main():
    profession_variants = ['analytic', 'аналитик', 'analyst', 'Аналитик']
    tasks = [get_vacancies(profession) for profession in profession_variants]

    await asyncio.gather(*tasks)


# if __name__ == '__main__':
# asyncio.run(main())
#
# res = dict(sorted(
#         result.items(),
#         key=lambda item: item[1]['published_at']
#     ))
# print(res)

def get_vacs():
    asyncio.run(main())
    res = dict(sorted(
        result.items(),
        key=lambda item: item[1]['published_at']
    ))
    vacs = {'vacancies':[*res.values()]}
    return vacs

get_vacs()
    # for vac in result.values():
    #     print(f"Название: {vac['title']}")
    #     print(f"Описание: {vac['description']}")
    #     print(f"Навыки: {vac['skills']}")
    #     print(f"Компания: {vac['company']}")
    #     print(f"Оклад: {vac['salary_info']}")
    #     print(f"Регион: {vac['region']}")
    #     print(f"Дата публикации: {vac['published_at']}")
    #     print("-" * 40)
