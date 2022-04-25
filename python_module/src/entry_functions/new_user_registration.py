# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
import sqlq.sql_queries
from sqlite3 import Error
from entry_functions.new_user_registration_functions import new_user_reg_get_login, new_user_reg_get_password

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


def registration():
    login = new_user_reg_get_login.get_login()
    password = new_user_reg_get_password.get_password()

    new_user_password_confirmation_input = input("Введите свой новый пароль еще раз: ")

    while new_user_password_confirmation_input != password:
        print('Введенные пароли не сходятся. Попробуйте еще раз.')
        new_user_password_confirmation_input = input("Введите свой новый пароль еще раз: ")
        if new_user_password_confirmation_input == password:
            break

    add_new_user = f"""
        INSERT INTO
            users (login_name, password, rank)
        VALUES
            ('{login}', '{password}', 'slave')
        """
    sqlq.sql_queries.execute_query_registration(connect_to_db, add_new_user)
