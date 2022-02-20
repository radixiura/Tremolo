import sqlq.sql_queries
from sqlite3 import Error
from entry_functions.new_user_registration_functions import new_user_registration_get_loginpassword

# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db


def registration():
    login = new_user_registration_get_loginpassword.new_user_registration_get_login()
    password = new_user_registration_get_loginpassword.new_user_registration_get_password()



    new_user_password_confirmation_input = input("Введите свой новый пароль еще раз: ")

    while new_user_password_confirmation_input != password:
        print('Введенные пароли не сходятся. Попробуйте еще раз.\n')
        if new_user_password_confirmation_input == password:
            break
    else:
        print("успешная регистрация")


    add_new_user = f"""
        INSERT INTO
            users (login_name, password, rank)
        VALUES
            ('{login}', '{password}', 'slave')
        """
    sqlq.sql_queries.execute_query_registration(connect_to_db, add_new_user)
