# -*- coding: utf-8 -*-

from modules import functions
# from modules import postgresql_connection

# postgresql_connection.connect_postgresql()

functions.greeting()

user_answer = input('Вы уже имеете аккаунт?: ')

if user_answer == 'Да':
    functions.old_user_registration()
elif user_answer == "Нет":
    functions.new_user_registration()

functions.main_menu()
