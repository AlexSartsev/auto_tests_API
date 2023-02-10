#!/bin/usr/python
import requests
import time
import re

class Test_jokes():
	"""Тестирование всех запросов Чак Норрис"""

	def __init__(self, category):
		"""Объявление переменной категория"""
		self.category = category

	def test_create_all_categories_joke(self, category):
		"""Отправка запроса"""

		url = f"https://api.chucknorris.io/jokes/random?category={self.category}"
		print(url)
		result = requests.get(url)
		print("Статус код: " + str(result.status_code), "Категория: " + category, sep='\n')
		assert 200 == result.status_code
		if result.status_code == 200:
			print("Запрос прошел успешно!")
		else:
			print("Запрос не прошел")
		result.encoding = "utf-8"
		print(result.text)


def test_get_categories():
	"""Получение списка категорий"""
	url = "https://api.chucknorris.io/jokes/categories"
	result = requests.get(url)
	string = result.text
	lst = re.split(r"\W+", string)
	return lst[1:len(lst)-1]

lst_categories = test_get_categories()

"""Поочередный перебор элементов списка и передача их в класс"""
for i in range(len(lst_categories)):
	jokes = Test_jokes(lst_categories[i])
	jokes.test_create_all_categories_joke(lst_categories[i])
	print()
	time.sleep(5)
