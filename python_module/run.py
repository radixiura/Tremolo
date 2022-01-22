# -*- coding: utf-8 -*-

# Connecting a file with functions
import os
import subprocess
import sys
from sys import platform
from functions import greetings, new_user_registration, user_authentication
from main_menu_modules import main_menu

import sqlite3
from sqlite3 import Error


def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Connection to SQLite DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection


connection = create_connection("C:\\sm_app.sqlite")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")


create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  login_name TEXT NOT NULL,
  password TEXT,
);
"""


create_messages_table = """
CREATE TABLE IF NOT EXISTS comments (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  text TEXT NOT NULL, 
  user_id INTEGER NOT NULL,  
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

create_diary_table = """
CREATE TABLE IF NOT EXISTS likes (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  user_id INTEGER NOT NULL, 
  post_id integer NOT NULL, 
  FOREIGN KEY (user_id) REFERENCES users (id) FOREIGN KEY (post_id) REFERENCES posts (id)
);
"""

execute_query(connection, create_messages_table)
execute_query(connection, create_diary_table)


execute_query(connection, create_users_table)


# В переменную user_answer вносим возвращаемое значение функции приветствия (0/1)
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
