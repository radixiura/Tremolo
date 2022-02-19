import sqlite3
from sqlite3 import Error


# Подключение к базе данных
def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        print("Подключение к базе данных прошло успешно.")
    except Error as e:
        print(f"Ошибка '{e}'. Не удалось подключиться к базе данных")
    return connection
# В переменную connection помещен скрипт создания подключения к БД
connection_to_db = create_connection("C:\\Users\\Radix\\Desktop\\tremolo_db.sqlite")

# Запросы к БД
#  Создание базы данных пользователей
def execute_query_create_users_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("База данных пользователей создана успешно!")
    except Error as e:
        print(f"Ошибка '{e}'. База данных пользователей не создалась!")


#  Создание базы данных сообщений
def execute_query_create_messages_table(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("База данных сообщений создана успешно!")
    except Error as e:
        print(f"Ошибка '{e}'. Регистрация не удалась!")


#  Регистрация
def execute_query_registration(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Вы были успешно зарегистрированы!")
    except Error as e:
        print(f"Ошибка '{e}'. Регистрация не удалась!")



#  Добавление сообщения
def execute_query_insert_into_messages(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Сообщение успешно добавлено!")
    except Error as e:
        print(f"Ошибка '{e}'. Регистрация не удалась!")


#  Обновление информации
def execute_query_renew(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запись успешно обновлена!")
    except Error as e:
        print(f"Ошибка '{e}'. Регистрация не удалась!")


#  Удаление информации
def execute_query_del(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Запись успешно удалена!")
    except Error as e:
        print(f"Ошибка '{e}'. Регистрация не удалась!")


def execute_read_query(connection, query):
    cursor = connection.cursor()
    result = None
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        print(f"The error '{e}' occurred")



# Создание первичных таблиц
# Создание таблицы пользователей
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  login_name TEXT NOT NULL,
  password TEXT NOT NULL,
  rank TEXT NOT NULL
);
"""
execute_query_create_users_table(connection_to_db, create_users_table)

# Создание таблицы сообщений
create_messages_table = """
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  message_text TEXT NOT NULL, 
  sender TEXT NOT NULL,
  recipient TEXT NOT NULL,  
  FOREIGN KEY (recipient) REFERENCES users (id)
);
"""
execute_query_create_messages_table(connection_to_db, create_messages_table)

# Заполнение данных в таблице сообщений
create_messages_info = """
INSERT INTO
  messages (message_text, sender, recipient)
VALUES
  ("kosovojesrbjia", "bigdaddy", 1),
  ("ohrlyfuck!", "joplej", 2);
"""
execute_query_insert_into_messages(connection_to_db, create_messages_info)
# Конец секции "Создание первичных таблиц" #


# Обновление записи в БД
update_message_text = """
UPDATE
  messages
SET
  message_text = "The weather has become pleasant now"
WHERE
  id = 2
"""
execute_query_renew(connection_to_db, update_message_text)

# Запрос удаления записи из БД
delete_comment = "DELETE FROM messages WHERE id = 5"
execute_query_del(connection_to_db, delete_comment)
