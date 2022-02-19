import sqlq.sql_queries
from sqlite3 import Error
# Скрипт создания подключения к бд
connect_to_db = sqlq.sql_queries.connection_to_db





def new_user_registration():
    new_user_login = input("Самое время зарегистрироваться. Введите свой новый логин:  ")
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

    # Добавление нового пользователя после успешной регистрации
    add_new_user = f"""
    INSERT INTO
      users (login_name, password, rank)
    VALUES
      ('{new_user_login}', '{new_user_password_confirmation}', 'slave')
    """
    sqlq.sql_queries.execute_query_registration(connect_to_db, add_new_user)
