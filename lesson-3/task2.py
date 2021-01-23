"""
2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
имя,
фамилия,
год рождения,
город проживания,
email,
телефон.
Функция должна принимать параметры как именованные аргументы.
Реализовать вывод данных о пользователе одной строкой.
"""


def inputData(var_name):
    return input(f'Введите {var_name} ')


def updateUser():
    name= inputData('Имя')
    surname = inputData('Фамилию')
    birthday = inputData('Дату рождения')
    city = inputData('Город')
    email = inputData('email')
    mobile = inputData('Номер телефона')
    return (name, surname, birthday, city, email, mobile)


def printUserData(name, surname, bithday, city, email, mobile):
    print(name, surname, bithday, city, email, mobile)


printUserData(*updateUser())