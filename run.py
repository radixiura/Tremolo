import os
import sys
import psycopg2
from psycopg2 import OperationalError

def create_connection(db_name, db_user, db_password, db_host, db_port):
    connection = None
    try:
        connection = psycopg2.connect(
            database = db_name,
            user = db_user,
            password = db_password,
            host = db_host,
            port = db_port,
        )
        print('Connection to PostgreSQL DB sucessful')
    except OperationalError as e:
        print(f"The error '{e}' occured")
    return connection

connection = create_connection("postgres", "postgres", "serv313", "127.0.0.1", "5432")

def create_database(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed successfully")
    except OperationalError as e:
        print(f"The error '{e}' occurred")

create_database_query = "CREATE DATABASE sm_app"
create_database(connection, create_database_query)

connection = create_connection(
    "sm_app", "postgres", "abc123", "127.0.0.1", "5432"
)

def execute_query(connection, query):
    connection.autocommit = True
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Query executed sucessfully")
    except OperationalError as e:
        print(f"The error '{e}' has occured")

create_users_table = """
CREATE TABLE IF NOT EXISTS users(
    id SERIAL PRIMARY KEY,
    login TEXT NOT NULL,
    password TEXT NOT NULL,
    age INTEGER,
    info TEXT
)
"""

execute_query(connection, create_users_table)


print('Привет!')
print('Рад видеть тебя.')
answer1 = input('Ты уже имеешь аккаунт?: ')
if answer1 == 'Да':
    print('Отлично.')
    old_user_login = input("Введите ваш логин: ")
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')

    print('Ваш логин - ' + old_user_login)
    old_user_password = input("Введите ваш пароль: ")

    # if old_user_password exist in DB:
    #   pass
    # else:
    #   print('Пароль введен неверно. Попробуете ввести пароль еще раз?: ')

    def menu():
        print('Выбери, что бы ты хотел сделать?')
        print('Отправить сообщение - 1')
        print('Узнать курс BTC - 2')
        print('Узнать свой ip - адрес - 3')
        print('Узнать свои настройки сети - 4')
        print('Завершить работу - 5')
        print('Связаться с разработчиком - 0')


    p = menu()
else:
    print('Думаю, тебе стоит зарегистрироваться.')
    new_user_login = input('Введи свой новый логин')
    # while new_user_login exists in BD
    # print('Этот логин уже занят')
    # print('Попробуйте ввести другой')
    # new_user_login = input()
    # if new_user_login not exists in BD:
    # break
    print('Ваш новый логин - ', new_user_login)
    print('Самое время придумать пароль!')
    new_user_password = input('Введи свой новый пароль')
    print('Подтвердите ваш пароль')
    new_user_password_confirmation = input()
    while new_user_password != new_user_password_confirmation:
        print('Введенные пароли не совпадают. Попробуйте еще раз ввести пароль')
        new_user_password_confirmation = input()
        if new_user_password_confirmation == new_user_password:
            break
            continue
    print('Отлично, ты зарегистрирован.')


    def menu():
        print('Выбери, что бы ты хотел сделать?')
        print('Написать другу - 1')
        print('Узнать курс BTC - 2')
        print('Узнать свой ip - адрес - 3')
        print('Узнать свои настройки сети - 4')
        print('Завершить работу - 5')
        print('Связаться с разработчиком - 0')

if user_choice == 1:
    print('Введи логин своего знакомого')
    new_request = input()
    # if new_request exists in BD and everything is ok:
    # print('Соединение успешно установлено.')
    # Начало переписки
    # if new_request not exists in BD:
    # print('Данный логин не найден.')
elif user_choice == 2:
    print('Актуальный курс биткоина')
    # api
elif user_choice == 3:
    print("Ваш текущий ip-адрес")
    # api
elif user_choice == 4:
    print('Ваши текущие настройки сети')
    # api
elif user_choice == 5:
    print('До свидания!')
    exit()
elif user_choice == 0:
    print('Реще')
    # api
