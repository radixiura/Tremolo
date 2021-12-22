# -*- coding: utf-8 -*-

# Connecting a file with functions
import subprocess
import sys
from functions import new_user_registration, user_authentication
from main_menu_modules import main_menu

# from modules import postgresql_connection
# postgresql_connection.connect_postgresql()

result = subprocess.run([r"C:\Users\Radix\Desktop\Tremolo\python_module\modules", "-c"])

print("Здравствуйте!")
user_answer = input("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ")
checking = True
while checking:
    if user_answer == "0":
        new_user_registration.new_user_registration()
        user_authentication.user_authentication()
        main_menu.main_menu_buttons()
    elif user_answer == "1":
        user_authentication.user_authentication()
        main_menu.main_menu_buttons()
    else:
        print("Ошибка. Вы ввели что - то странное.")
