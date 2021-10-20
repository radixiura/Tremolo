# -*- coding: utf-8 -*-

# Connecting a file with functions
from modules import functions

# from modules import postgresql_connection
# postgresql_connection.connect_postgresql()

print("Привет!")

# Choosing between login and registration

checking = True

while checking:
    user_answer = int(input('Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: '))

    if user_answer == 1:
        functions.new_user_registration()
        functions.main_menu()
    elif user_answer == 0:
        functions.old_user_authentication()
        functions.main_menu()
    else:
        print("Вы ввели что - то странное!")
        user_answer = input('Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ')
