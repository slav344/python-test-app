# class Restaurant:
#     def __init__(self, cuisine_type, name):
#         self.cuisine_type = cuisine_type
#         self.name = name
#
#     def describe_restaurant(self):
#         print(f" {self.cuisine_type} {self.name}")
#
#     def open_restaurant(self):
#         print("The restaurant is open")
#
#
# my_restaurant = Restaurant("Gourmet restaurant", "Victoria")
# my_restaurant.describe_restaurant()
#
#
# my_restaurant2 = Restaurant("Food truck", "BMB")
# my_restaurant2.describe_restaurant()
#
# my_restaurant3 = Restaurant("Fast-food restauran","Burger")
# my_restaurant3.describe_restaurant()
# my_restaurant.open_restaurant()

#
# class User:
#     def __init__(self, first_name, last_name, age, profession, work_company):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.profession = profession
#         self.work_company = work_company
#
#     def describe_user(self):
#         print(f"\n{self.first_name},\n{self.last_name},\n{self.age},\n{self.profession},\n{self.work_company}")
#
#     def greet_user(self):
#         print("HELLO FRIEND")
#
#
# my_user = User("Ющ", "Андрій", 34, "шофер", "BMB")
# my_user.describe_user()
#
#
# my_user1 = User("GF", "Yura", 23, "taxi driver","MTS" )
# my_user1.describe_user()
#
# my_user.greet_user()
#
# class Restaurant:
#     def __init__(self, cuisine_type, name, number_served):
#         self.cuisine_type = cuisine_type
#         self.name = name
#         self.number_served = 0
#
#     def describe_restaurant(self):
#         print(f" {self.cuisine_type} {self.name},Number served {self.number_served}")
#
#     def set_number_served(self, number):
#         self.number_served = number
#
#     def increment_number_served(self, numbers):
#         self.number_served += numbers
#
# my_restaurant = Restaurant("Gourmet restaurant", "Victoria", 0)
# my_restaurant.describe_restaurant()
# my_restaurant.number_served = 23
# my_restaurant.describe_restaurant()
# my_restaurant.set_number_served(45)
# my_restaurant.describe_restaurant()
# my_restaurant.increment_number_served(50)
# my_restaurant.describe_restaurant()
# import random
#
#
# class Die:
#     __sides: int = 6
#
#     def roll_die(self):
#         print(random.randint(1, self.__sides))
#
#
# die = Die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()
# die.roll_die()

# import random
#
# list = [4, 56, 34, 89, 90, 12, 9, 86, 31, 7, "F", "W", "M", "X", "Q"]
# print("Winning lottery numbers", random.sample(list, 4))

# my_ticket = [56, 78, 90, 675, 321, 12, 6]
# random_number = random.sample(my_ticket, 1)
# print(random_number)
#
# for ticket in my_ticket:
#     if random_number == [ticket]:
#         print("You won: ", ticket)
#         print(f"Were {my_ticket.index(ticket)} unsuccessful tickets")
#         break
#     else:
#         print("Please try again")
#


# with open('pi_digits.txt') as file_object:
#     contents = file_object.read()
# print(contents.rstrip())
#
# 10.1
# filname = "learning_python.txt"
#
# with open(filname) as file_object:
#     contents = file_object.read()
# print(contents)
#
# print("==========================================================================")
#
# with open(filname) as file_object:
#     for line in file_object:
#         print(line)
#
# print("==========================================================================")
#
# with open(filname) as file_object:
#     list = file_object.readlines()
#
# for line in list:
#     print(line.rstrip())

# Число Пі....
# filname = "pi_digits.txt"
#
# with open(filname) as file_object:
#     lines = file_object.readlines()
#
# pi_string = ''
# for line in lines:
#     pi_string += line.strip()
#
# birthday = input("Enter your birthay,in the form mmddyy: ")
# if birthday in pi_string:
#     print("Your birthey appears in the dijits of pi !")
# else:
#     print("Your birthay does not appears in the dijits of pi !")


# 10-3
# name = input("You name is: ")
# filename = "pi_digits.txt"
# with open(filename, 'w') as file_object:
#     file_object.write(name)

# 10-4
# polling_active = True
#
# while polling_active:
#     name = input("Please enter your name: ")
#     print(f"Hello,{name}")
#
#     filname = "pi_digits.txt"
#     with open(filname, "a") as file_object:
#         file_object.write(f"\n{name}")

# 10-6
# print("Give me two numbers and I will add them")
# print("Enter 'q'to quit")
#
# while True:
#     first_number = input("\nFirst number: ")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number: ")
#     if second_number == 'q':
#         break
#
#     try:
#         answer = int(first_number) + int(second_number)
#
#     except ValueError:
#         print("Not numeric input")
#     else:
#         print(answer)

# 10 - 7
#
# while True:
#     first_number = input("\nFirst number")
#     if first_number == 'q':
#         break
#     second_number = input("\nSecond number")
#     if second_number == 'q':
#         break
#
#     try:
#         answer = int(first_number) + int(second_number)
#
#     except ValueError:
#         pass
#     else:
#         print(answer)


# 10 - 8

# cats_name = 'cats.txt'
# dogs_name = 'dogs.txt'
#
# with open('cats.txt') as file_obgect:
#     cats = file_obgect.read()
#     print(cats)
#
# try:
#     with open('dogs.txt') as file_obgect:
#         dogs = file_obgect.read()
#         print(dogs)
# except FileNotFoundError:
#     print("Файл не знайдено!")


# import requests
#
# url = 'https://httpbin.org/get'
# response = requests.get(url)
# print(type(response))
# print(dir(response))

# print(response.headers, 'headers')
# print(response.status_code, 'status_code')
# print(response.request, 'request')

# print(response.content,'content')
# print(response.text, 'text')
# print(response.json(), 'json')


# import requests
#
# url = 'https://www.youtube.com/results'
# guery = {'searth_guery': 'audi'}
# response = requests.get(url, params=guery)
#
# print(response.status_code, 'status_code')
# print(response, url, 'url')


# url = 'https://httpbin.org/get'
# # url = 'https://httpbin.org/post'
# # query = [('serth_query', 'audi')]
# # response = requests.post(url, data=query)
# response = requests.get(url)
#
# # print(response.status_code, 'status_code')
# # print(response.url, 'url')
# # print(response.json(), 'json')
# print(f"Status code: {response.status_code}")
# print(f"Response: {response.json()}")

# response = requests.put(url, data=query)
# response = requests.patch(url, data=query)
# response = requests.delete(url)
# response = requests.head(url)
# response = requests.options(url)

# import requests
#
# url = 'http://www.lib.ru/INOFANT/STARGZHON/okkam.txt'
# response = requests.get(url)
#
# with open('story.txt', 'w') as file:
#     file.write(response.text)

import Network

user_controller = Network.UserController()
user_response = user_controller.get_result()
print(user_response)
