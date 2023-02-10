#!/bin/usr/python
import requests
import time

class Test_new_location():

	"""Работа с локацией"""
	def __init__(self):
		"""Инициализация атрибутов"""
		self.base_url = "https://rahulshettyacademy.com"
		self.key = "?key=qaclick123"

	def test_create_new_location(self):
		"""Создание новой локации"""
		post_resource = "/maps/api/place/add/json"

		post_url = self.base_url + post_resource + self.key
		print(post_url)

		json_for_create_new_location = {
		"location": {
			"lat": -38.383494,
			"lng": 33.427362
		}, "accuracy": 50,
		"name": "Frontline house",
		"phone_number": "(+91) 983 893 3937",
		"address": "29, side layout, cohen 09",
		"types": [
			"shoe park",
			"shop"
		],
		"website": "http://google.com",
		"language": "French-IN"
		}

		result_post = requests.post(post_url, json = json_for_create_new_location)
		assert 200 == result_post.status_code
		print("Код ответа: " + str(result_post.status_code))
		print("Успешно! Создана новая локация")
		check_post = result_post.json()
		place_id = check_post.get("place_id")
		writing_to_file = open('file.txt', 'a')
		writing_to_file.write(place_id + "\n")
		writing_to_file.close()

	def test_new_get_location(self):
		"""Проверка создания новой локации. Метод GET"""
		read_to_file = open("file.txt", "r")
		place_id_from_file = read_to_file.read(32)
		read_to_file.close()
		print(place_id_from_file)
		get_resource = "/maps/api/place/get/json"
		get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id_from_file
		print(get_url)
		result_get = requests.get(get_url)
		print(result_get.text)
		assert 200 == result_get.status_code
		print("Код ответа: " + str(result_get.status_code))
		print("Успешно! Проверка создания новой локации прошла успешно")

new_place = Test_new_location()
for i in range(5):
	new_place.test_create_new_location()
	print()
new_place.test_new_get_location()
