import sqlq.sql_queries
from sqlite3 import Error
# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


def user_authentication():
    login = input("Введите ваш логин: ")
    x = f"SELECT ALL login_name FROM users WHERE login_name='{login}'"
    check_x = execute_read_query(connect_to_db, x)
    if check_x == None:
        print("Полный высад")
    else:
        print("Вайb")
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')
    password = input("Введите ваш пароль: ")
    print(f"{login}, вы успешно вошли.")
    # if old_user_password exist in DB:
    #   pass
    # else:
    #   print('Пароль введен неверно. Попробуете ввести пароль еще раз?: ')
    return login, password
