# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
import sqlq.sql_queries
from sqlite3 import Error
from entry_functions.user_auth_functions import user_auth_get_login, user_auth_get_password

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db

# Часть 1
# 1.1 Функция входа пользователя
def auth_func():
    # 1.1.1 Получение логина пользователя
    login = user_auth_get_login.get_login()
    # 1.1.2 Получение пароля пользователя
    password = user_auth_get_password.get_password()


    # 1.1.3 Получение пароля пользователя
    password = user_auth_get_password.get_password()
    # 1.1.4 Запрос на проверку существования пароля
    query_for_check =  f"SELECT ALL password FROM users WHERE password='{password}'"
    password_checking = sqlq.sql_queries.execute_read_query(connect_to_db, query_for_check)

    password_correct = False
    while not password_correct:
        if password_checking == []:
            print("Логин или пароль введены неправильно! Попробуйте еще раз")
            user_authentication()
        else:
            print(f"{login}, вы успешно вошли.")
            password_correct = True
    return login, password


