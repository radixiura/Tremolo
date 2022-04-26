# Основной файл программы
# Содержание:

# -*- coding: utf-8 -*-

# Импорты
from entry_functions import greeting, new_user_registration, user_authentication
from main_menu_modules import main_menu

# Часть 1
# 1.1
user_answer_entry = greeting.greeting_function()
if user_answer_entry == "0":
    new_user_registration.registration()
elif user_answer_entry == "1":
    print("Отлично!")
else:
    print("Ошибка! Вы ввели что - то странное, попробуйте еще раз.")
    greeting.greeting_function()

# Часть 2
# 2.1
user_authentication.user_authentication()
main_menu.main_menu_buttons()
