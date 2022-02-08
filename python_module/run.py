# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error

from functions import greeting, new_user_registration, user_authentication
from main_menu_modules import main_menu


# Подключение к базе данных
def create_connection(path):
    connect_to_db = None
    try:
        connect_to_db = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connect_to_db


# В переменную connection помещаем скрипт подключения к БД
connection = create_connection("C:\\Users\\Radix\\Desktop\\tremolo_db.sqlite")


# Шаблоны выполнения запроса

# Стандартный запрос к БД
# Параметры функции: (Скрипт подключения к бд, будущий запрос)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Основная часть
# В переменную user_answer помещаем возвращаемое значение функции приветствия (0/1)
user_answer = greeting.greeting_function()

if user_answer == "0":
    # Вызов функции регистрации
    new_user_registration.new_user_registration()
    # Главное меню
    main_menu.main_menu_buttons()
elif user_answer == "1":
    print("Отлично!")
else:
    print("Ошибка. Вы ввели что - то странное.")

user_authentication.user_authentication()
main_menu.main_menu_buttons()
