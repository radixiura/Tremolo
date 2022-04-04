import sqlq.sql_queries
from sqlite3 import Error

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


def get_password():
    new_user_password = input("Введите ваш новый пароль: ")
    # Проверка достаточности длины пароля
    while len(new_user_password) < 8:
        print('Пароль должен содержать более 8ми символов. Попробуйте заново.')
        print("Введите свой новый пароль: ")
        new_user_password = input()
        if len(new_user_password) > 8:
            break
    return new_user_password
