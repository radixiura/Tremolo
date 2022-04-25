# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
import sqlq.sql_queries
from sqlite3 import Error

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db

# Часть 1
# 1.1 Функция входа пользователя
def user_authentication():
    # 1.1.1 Получение логина пользователя
    login = input("Введите логин: ")
    # 1.1.2 Запрос на проверку существования логина
    query_for_login_check = f"SELECT ALL login_name FROM users WHERE login_name='{login}'"
    login_checking = sqlq.sql_queries.execute_read_query(connect_to_db, query_for_login_check)

    login_correct = False
    while not login_correct:
        if login_checking == []:
            print("Логин введен неправильно! Попробуйте еще раз")
            user_authentication()
        else:
            print(f"{login}, вы успешно вошли.")
            login_correct = True


    # 1.1.3 Получение пароля пользователя
    password = input("Введите пароль: ")
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


