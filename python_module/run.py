# -*- coding: utf-8 -*-

import sqlite3
from sqlite3 import Error

from sqlq import sql_queries
from functions import greeting, new_user_registration, user_authentication
from main_menu_modules import main_menu

# Скрипт создания подключения к бд
connect_to_db = sql_queries.connection_to_db


# Подключение к базе данных
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


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
user_answer = greeting.greeting_function()
if user_answer == "0":
    new_user_registration.new_user_registration()
    main_menu.main_menu_buttons()
elif user_answer == "1":
    print("Отлично!")
else:
    print("Ошибка. Вы ввели что - то странное.")

user_authentication.user_authentication()
main_menu.main_menu_buttons()
# Конец секции "Основная часть" #
