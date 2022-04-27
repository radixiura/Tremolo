# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
import sqlq.sql_queries
from sqlite3 import Error

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


# Часть 1
# 1.1 Функция получения логина пользователя
def get_login():
    # 1.1.1 Получение логина пользователя
    user_login = input("Введите логин:  ")
    # 1.1.2 Запрос на проверку существования логина
    query_for_login_check = f"SELECT ALL login_name FROM users WHERE login_name='{user_login}'"
    user_login_checking = sqlq.sql_queries.execute_read_query(connect_to_db, query_for_login_check)

    user_login_correct = False
    while not user_login_correct:
        if user_login_checking == user_login:
            print('Успешно.')
            user_login_correct = True
        elif user_login_checking == []:
            print(f"Нет пользователя с логином {user_login}")
            get_login()
    return user_login
