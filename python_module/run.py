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


# Запрос на извлечение данных из БД
# Параметры функции: (Скрипт подключения к бд, будущий запрос)
def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

for user in users:
    print(user)


# Запрос на обновление информации в БД
select_message_destination = "SELECT destination FROM messages WHERE id = 2"
message_destination = execute_read_query(connection, select_message_destination)

for destination in message_destination:
    print(destination)

update_message_destination = """
UPDATE
  messages
SET
  destination = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection, update_message_destination)


# Шаблон обновления записи в БД
select_message_destination = "SELECT destination FROM messages WHERE id = 2"
message_destination = execute_read_query(connection, select_message_destination)

for destination in message_destination:
    print(destination)

update_message_destination = """
UPDATE
  messages
SET
  destination = "The weather has become pleasant now"
WHERE
  id = 2
"""
execute_query(connection, update_message_destination)

# Шаблон удаления записи из БД
delete_comment = "DELETE FROM messages WHERE id = 5"
execute_query(connection, delete_comment)


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
