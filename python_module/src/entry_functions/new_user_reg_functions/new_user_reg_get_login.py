# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
import sqlq.sql_queries
from sqlite3 import Error

import time

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


# Часть 1
# 1.1 Функция получения логина нового пользователя
def get_login():
    new_user_login = input("Самое время зарегистрироваться. Введите свой новый логин:  ")
    new_user_login_correct = False
    while not new_user_login_correct:
        if len(new_user_login) < 8:
            time.sleep(3)
            print('Логин должен содержать более 8ми символов. Попробуйте заново.')
            new_user_login = input("Введите свой новый логин еще раз:  ")
        else:
            print(f"Ваш новый логин: {new_user_login}")
            new_user_login_correct = True
    return new_user_login
