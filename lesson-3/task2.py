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


def input_data(var_name):
    return input(f'Введите {var_name} ')


def update_user():
    name = input_data('Имя')
    surname = input_data('Фамилию')
    birthday = input_data('Дату рождения')
    city = input_data('Город')
    email = input_data('email')
    mobile = input_data('Номер телефона')
    return (name, surname, birthday, city, email, mobile)


def print_user_data(name, surname, bithday, city, email, mobile):
    print(name, surname, bithday, city, email, mobile)


print_user_data(*update_user())