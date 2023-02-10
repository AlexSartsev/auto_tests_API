#!/bin/usr/python
import requests

class Test_API():

    """Отправка GET запроса для получения списка фильмов"""
    def test_get_list_films(get_url, category):
        result_get = requests.get(get_url)
        assert 200 == result_get.status_code
        print("Код ответа: " + str(result_get.status_code))
        check_get = result_get.json()
        parameter = check_get.get(category)
        return parameter



"""Сортировка списка на неповторяющиеся элементы"""
def sorted_list(lst):
    lst_characters = list()
    for i in range(len(lst)):
        if lst[i] not in lst_characters:
            lst_characters.append(lst[i])
    return lst_characters



"""Передача и получение тестовых данных в качестве параметров"""
print("Получение списка фильмов")
lst_films = Test_API.test_get_list_films('https://swapi.dev/api/people/4/', 'films')

print("Получение списка персонажей")
characters = list()
for link in range(len(lst_films)):
    characters += Test_API.test_get_list_films(lst_films[link], 'characters')

print("Получение и записывание в файл имён персонажей")
lst_characters = sorted_list(characters)
for person in range(len(lst_characters)):
    name = Test_API.test_get_list_films(lst_characters[person], 'name')
    file = open('characters.txt', 'a')
    file.write(name + '\n')
    file.close()