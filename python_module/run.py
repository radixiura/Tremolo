# -*- coding: utf-8 -*-

# Connecting a file with functions
import os
import subprocess
import sys
from sys import platform
from functions import greetings, new_user_registration, user_authentication
from main_menu_modules import main_menu

# В переменную user_answer вносим возвращаемое значение приветственной функции (0/1)
user_answer = greetings.greetings()

if user_answer == "0":
    new_user_registration.new_user_registration()
    user_authentication.user_authentication()
    main_menu.main_menu_buttons()
elif user_answer == "1":
    user_authentication.user_authentication()
    main_menu.main_menu_buttons()
else:
    print("Ошибка. Вы ввели что - то странное.")
