#!/bin/usr/python
import requests

class Test_new_location():

	"""Работа с локацией"""
	def __init__(self, string):
		"""Инициализация атрибутов"""
		self.string = string
		self.base_url = "https://rahulshettyacademy.com"
		self.key = "?key=qaclick123"

	def test_delete_location(self):
		"""Удаление локации"""
		delete_resource = "/maps/api/place/delete/json"

		delete_url = self.base_url + delete_resource + self.key
		print(delete_url)
		place_id = self.string.rstrip("\n\r")

		json_for_delete_location = {
		"place_id": place_id
		}
		result_delete = requests.delete(delete_url, json = json_for_delete_location)
		assert 200 == result_delete.status_code
		print("Код ответа: " + str(result_delete.status_code))
		print("Локация успешно удалена!")

	def test_put_location(self):
		"""Проверка локаций из файла"""
		get_resource = "/maps/api/place/get/json"
		place_id = self.string.rstrip("\n\r")
		get_url = self.base_url + get_resource + self.key + "&place_id=" + place_id
		print(get_url)
		result_get = requests.get(get_url)
		if result_get.status_code == 200:
			print("Код ответа: " + str(result_get.status_code))
			print("Проверка создания новой локации прошла успешно!")
			file_location = open("file_location.txt", "a")
			file_location.write(place_id + "\n")
			file_location.close()
		else:
			print("Код ответа: " + str(result_get.status_code))
			print("Данной локации не существует!")

def lst_file_line():
	"""Чтение файла и получение всех строк в виде списка"""
	read_to_file = open("file.txt", "r")
	lst = read_to_file.readlines()
	read_to_file.close()
	return lst

lst_lines = lst_file_line()

for delete in range(1, len(lst_lines), 2):
	new_place = Test_new_location(lst_lines[delete])
	new_place.test_delete_location()
	print()
for put in range(0, len(lst_lines)):
	new_place = Test_new_location(lst_lines[put])
	new_place.test_put_location()
	print()
