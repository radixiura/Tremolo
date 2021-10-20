# -*- coding: utf-8 -*-

# Connecting a file with functions
from modules import functions

# from modules import postgresql_connection
# postgresql_connection.connect_postgresql()
print("Привет!")
user_answer = input("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ")
checking = True
while checking:
    if user_answer == "0":
        functions.new_user_registration()
        functions.main_menu()
    elif user_answer == "1":
        functions.old_user_authentication()
        functions.main_menu()
    else:
        print("Ошибка. Вы ввели что - то странное.")
