# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
import sqlq.sql_queries
from sqlite3 import Error

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


def get_password():
    new_user_password = input("Введите ваш новый пароль: ")
    new_user_password_correct = False
    while not new_user_password_correct:
        if len(new_user_password) < 8:
            print('Пароль должен содержать более 8ми символов. Попробуйте заново.')
            new_user_password = input("Введите свой пароль еще раз:  ")
        else:
            print(f"Ваш новый пароль: {new_user_password}")
            new_user_password_correct = True
    return new_user_password


