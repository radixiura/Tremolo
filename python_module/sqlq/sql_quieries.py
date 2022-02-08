import sqlite3
from sqlite3 import Error


# Подключение к базе данных
def create_connection(path):
    connect_to_db = None
    try:
        connect_to_db = sqlite3.connect(path)
        print("Подключение к базе данных прошло успешно.")
    except Error as e:
        print(f"Ошибка '{e}'. Не удалось подключиться к базе данных")

    return connect_to_db


# В переменную connection помещен скрипт подключения к БД
connection = create_connection("C:\\Users\\Radix\\Desktop\\tremolo_db.sqlite")


# Шаблон запроса к БД
def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
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
execute_query(connection, create_users_table)

# Заполнение данных в таблице пользователей
create_users_info = """
INSERT INTO
  users (login_name, password, rank)
VALUES
  ('bigdaddy', 'porridge1', 'principale'),
  ('joplej', 'gavnostar0', 'slave');
"""
execute_query(connection, create_users_info)

# Создание таблицы сообщений
create_messages_table = """
CREATE TABLE IF NOT EXISTS messages (
  id INTEGER PRIMARY KEY AUTOINCREMENT, 
  msg TEXT NOT NULL, 
  destination TEXT NOT NULL,
  user_id INTEGER NOT NULL,  
  FOREIGN KEY (user_id) REFERENCES users (id)
);
"""
execute_query(connection, create_messages_table)

# Заполнение данных в таблице сообщений
create_messages_info = """
INSERT INTO
  messages (msg, destination, user_id)
VALUES
  ("Happy", "I am feeling very happy today", 1),
  ("Hot Weather", "The weather is very hot today", 2),
  ("Help", "I need some help with my work", 2),
  ("Great News", "I am getting married", 1),
  ("Interesting Game", "It was a fantastic game of tennis", 5),
  ("Party", "Anyone up for a late-night party today?", 3);
"""
execute_query(connection, create_messages_info)
# Конец секции "Создание первичных таблиц" #


# Вторичные запросы V
# Запрос на извлечение данных из БД
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
users = execute_read_query(connection, select_users)
for user in users:
    print(user)

# Запрос на обновление информации в БД
select_message_destination = "SELECT destination FROM messages WHERE id = 2"
message_destination = execute_read_query(connection, select_message_destination)

for destination in message_destination:
    print(destination)

update_message_destination = """
UPDATE
  messages
SET
  destination = "The weather has become pleasant now"
WHERE
  id = 2
"""
execute_query(connection, update_message_destination)

# Запрос удаления записи из БД
delete_comment = "DELETE FROM messages WHERE id = 5"
execute_query(connection, delete_comment)
