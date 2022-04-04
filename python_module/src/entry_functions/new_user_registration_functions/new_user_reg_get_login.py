import sqlq.sql_queries
from sqlite3 import Error

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


def get_login():
    new_user_login = input("Самое время зарегистрироваться. Введите свой новый логин:  ")
    while len(new_user_login) < 8:
        print('Логин должен содержать более 8ми символов. Попробуйте заново.')
        print("Введите свой новый логин: ")
        new_user_login = input()
        if len(new_user_login) > 8:
            break
    return new_user_login
