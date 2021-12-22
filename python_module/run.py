# -*- coding: utf-8 -*-

# Connecting a file with functions
import os
import subprocess
import sys
from sys import platform
from functions import new_user_registration, user_authentication
from main_menu_modules import main_menu

# from modules import postgresql_connection
# postgresql_connection.connect_postgresql()

if platform == "linux" or platform == "linux2":
    print('ln')
elif platform == "darwin":
    print('qdwd')
elif platform == "win32":
    print('wdd')

os.system(r"modules\dist\design.exe")

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
