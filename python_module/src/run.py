# -*- coding: utf-8 -*-

from functions import greeting, new_user_registration, user_authentication
from main_menu_modules import main_menu

# Основная часть
# Вызов функции приветствия и передача значения в переменную user_answer
user_answer = greeting.greeting_function()
if user_answer == "0":
    new_user_registration.new_user_registration()
elif user_answer == "1":
    print("Отлично!")
else:
    print("Ошибка. Вы ввели что - то странное.")

user_authentication.user_authentication()
main_menu.main_menu_buttons()
# Конец секции "Основная часть" #
