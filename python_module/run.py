# -*- coding: utf-8 -*-

# Connecting a file with functions
from modules import functions

# from modules import postgresql_connection
# postgresql_connection.connect_postgresql()

print("Привет!")

# Choosing between login and registration

user_answer = input('Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ')
if user_answer.lower() == "1":
    functions.old_user_registration()
if user_answer.lower() == "2":
    functions.new_user_registration()
else:
    user_second_answer = input('''Мы не совсем поняли ваш ответ. 
    Введите 1 если вы уже имеете аккаунт; 0 - если хотите зарегистрироваться.''')
    while user_second_answer != "1" or "0":
        user_second_answer = input('''Мы не совсем поняли ваш ответ.
        Введите 1 если вы уже имеете аккаунт; 0 - если хотите зарегистрироваться.''')
        if user_answer == 1 or 2:
            break
