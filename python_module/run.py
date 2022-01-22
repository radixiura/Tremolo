# -*- coding: utf-8 -*-

import os
import sqlite3
from sqlite3 import Error
import subprocess
import sys
from sys import platform

from functions import greetings, new_user_registration, user_authentication
from main_menu_modules import main_menu


# Подключение к базе данных
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


# В переменную connection помещаем скрипт подключения к БД
connection = create_connection("C:\\sm_app.sqlite")


# Шаблон выполнения запроса
# Параметры функции: (Скрипт подключения к бд, будущий запрос)
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


# Создание таблицы пользователей со столбцами (id, логин, пароль, ранг)
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  login_name TEXT NOT NULL,
  password TEXT,
  rank TEXT
);
"""

create_users = """
INSERT INTO
  users (login_name, password, rank)
VALUES
  ('James', 25, 'male'),
  ('Leila', 32, 'female'),
  ('Brigitte', 35, 'female'),
  ('Mike', 40, 'male'),
  ('Elizabeth', 21, 'female');
"""


# Создание таблицы сообщений со столбцами (id, сообщение, адресат, id адресанта)
create_messages_table = """
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  msg TEXT, 
  destination TEXT,
  user_id INTEGER NOT NULL,  
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""

create_messages = """
INSERT INTO
  messages (msg, destination, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""

# Запрос [Создание таблицы пользователей]
# Параметры функции: (Скрипт подключения к бд, создание таблицы пользователей)
execute_query(connection, create_users_table)

# Запрос [Создание таблицы сообщений]
# Параметры функции: (Скрипт подключения к бд, создание таблицы сообщений)
execute_query(connection, create_messages_table)

execute_query(connection, create_users)

execute_query(connection, create_messages)


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


update_message_destination = """
UPDATE
  messages
SET
  destination = "The weather has become pleasant now"
WHERE
  id = 2
"""

execute_query(connection, update_message_destination)


select_users = "SELECT * from users"
users = execute_read_query(connection, select_users)

select_message_destination = "SELECT destination FROM messages WHERE id = 2"

post_description = execute_read_query(connection, select_message_destination)



delete_comment = "DELETE FROM comments WHERE id = 5"
execute_query(connection, delete_comment)

for description in post_description:
    print(description)


for user in users:
    print(user)


# В переменную user_answer помещаем возвращаемое значение функции приветствия (0/1)
user_answer = greetings.greetings()

if user_answer == "0":
    # Вызов функции регистрации
    new_user_registration.new_user_registration()
    # Вызов функции аутентификации
    user_authentication.user_authentication()
    # Главное меню
    main_menu.main_menu_buttons()
elif user_answer == "1":
    # Вызов функции аутентификации
    user_authentication.user_authentication()
    # Главное меню
    main_menu.main_menu_buttons()
else:
    print("Ошибка. Вы ввели что - то странное.")
