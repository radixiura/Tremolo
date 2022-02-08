import sqlq.sql_queries
from sqlite3 import Error
# Алиас скрипта подключения к бд
connect = sqlq.sql_queries.connection


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")


select_users = "SELECT ALL login_name FROM users"
users = execute_read_query(connect, select_users)
for user in users:
    print(user)

# Создать массив answers ответов БД (логины пользователей)


def new_user_registration():
    # Логин нового пользователя
    new_user_login = input("Самое время зарегистрироваться. Введите свой новый логин:  ")
    # if new_user_login exist in answers
        # print('Этот логин уже занят!')
    # Проверка достаточности длины логина
    while len(new_user_login) < 8:
        print('Логин должен содержать более 8ми символов. Попробуйте заново.')
        new_user_login = input()
        if len(new_user_login) > 8:
            break

    # Пароль нового пользователя
    new_user_password = input("Введите ваш новый пароль: ")
    # Проверка достаточности длины пароля
    while len(new_user_password) < 8:
        print('Пароль должен содержать более 8ми символов. Попробуйте заново.')
        new_user_password = input()
        if len(new_user_password) > 8:
            break

    # Подтверждение нового пароля
    new_user_password_confirmation = input("Введите свой новый пароль еще раз: ")
    while new_user_password != new_user_password_confirmation:
        print('Введенные пароли не сходятся. Попробуйте еще раз.\n')
        new_user_password_confirmation = input()
        if new_user_password_confirmation == new_user_password:
            break

    # Создание таблицы пользователей
    sqlq.sql_queries.execute_query(connect, sqlq.sql_queries.create_users_table)

    # Добавление нового пользователя
    new_user = f"""
    INSERT INTO
      users (login_name, password, rank)
    VALUES
      ('{new_user_login}', '{new_user_password_confirmation}', 'slave')
    """
    sqlq.sql_queries.execute_query(connect, new_user)
