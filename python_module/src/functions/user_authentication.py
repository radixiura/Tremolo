import sqlq.sql_queries
from sqlite3 import Error
# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db

def user_authentication():
    login = input("Введите логин: ")
    query_for_login_check = f"SELECT ALL login_name FROM users WHERE login_name='{login}'"
    login_checking = sqlq.sql_queries.execute_read_query(connect_to_db, query_for_login_check)
    if login_checking == []:
        def x():
            x = 1
            return x
    password = input("Введите пароль: ")
    query_for_check =  f"SELECT ALL password FROM users WHERE password='{password}'"
    password_checking = sqlq.sql_queries.execute_read_query(connect_to_db, query_for_check)
    if password_checking == []:
        print("Логин или пароль введены неправильно! Попробуйте еще раз \n")
        user_authentication()
    x_storage = x()
    if x_storage == 1:
        print("Логиныч или пароль введены неправильно! Попробуйте еще раз \n")
        user_authentication()
    else:
        print("все ахуен")
    print(f"{login}, вы успешно вошли.")
    return login, password
