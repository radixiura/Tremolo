from modules import functions
# from modules import postgresql_connection

# postgresql_connection.connect_postgresql()

functions.greeting()

user_answer = input('Ты уже имеешь аккаунт?: ')

if user_answer == 'Да':
    functions.old_user_registration()
elif user_answer == "Нет":
    functions.new_user_registration()


functions.main_menu()

user_choice = input("Выберите действие: ")

if user_choice == "1":
    functions.menu1()
elif user_choice == "2":
    functions.menu2()
elif user_choice == "3":
    functions.menu3()
elif user_choice == "4":
    functions.menu4()
elif user_choice == "5":
    functions.menu5()
elif user_choice == "6":
    functions.menu6()
elif user_choice == "0":
    print('Значит, ты выбрал смерть...')
