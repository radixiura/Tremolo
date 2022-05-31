# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
import time


from entry_functions import greeting, new_user_registration, user_authentication
from main_menu_modules import main_menu

# Часть 1
# 1.1
user_answer_entry = greeting.greeting_func()
time.sleep(3)
# 1.2
user_answer_entry_correct = False
while not user_answer_entry_correct:
    if user_answer_entry == "0":
        new_user_registration.registration_func()
        user_answer_entry_correct = True
    elif user_answer_entry == "1":
        print("Отлично!")
        user_answer_entry_correct = True
    else:
        print("Ошибка! Вы ввели что - то странное, попробуйте еще раз.")
        greeting.greeting_func()


# Часть 2
# 2.1
user_authentication.authentication_func()
main_menu.main_menu_buttons()
