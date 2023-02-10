#!/bin/usr/python
import requests
import re

class Test_jokes():
	"""Тестирование запроса пользователя"""

	def __init__(self, category):
		"""Объявление переменной запроса пользователя"""
		self.category = category

	def test_create_category_joke(self, category):
		"""Отправка запроса"""
		url = f"https://api.chucknorris.io/jokes/random?category={self.category}"
		print(url)
		result = requests.get(url)
		print("Статус код: " + str(result.status_code))
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

def input_request(lst):
	"""Получение запроса от пользователя"""
	while True:
		request = input("Введите запрос: ")

		if request in lst_categories:
			return request
		else:
			print("Данного запроса нет в списке")
			print("Запросы: 'animal', 'career', 'celebrity', 'dev', 'explicit', 'fashion', 'food', 'history', 'money', 'movie', 'music', 'political', 'religion', 'science', 'sport', 'travel'")

lst_categories = test_get_categories()
us_request = input_request(lst_categories)

jokes = Test_jokes(us_request)
jokes.test_create_category_joke(us_request)
