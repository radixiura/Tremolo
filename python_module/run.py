import functions
import postgresql_connection

postgresql_connection.connect_postgresql()

functions.greeting()

user_answer = input('Ты уже имеешь аккаунт?: ')

if user_answer == 'Да':
    print('Отлично.')
    old_user_login = input("Введите ваш логин: ")
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')
    print('Ваш логин: ' + old_user_login)
    old_user_password = input("Введите ваш пароль: ")
    # if old_user_password exist in DB:
    #   pass
    # else:
    #   print('Пароль введен неверно. Попробуете ввести пароль еще раз?: ')
else:
    print('Думаю, тебе стоит зарегистрироваться.')
    new_user_login = input('Введи свой новый логин: ')
    # while new_user_login exists in BD
    # print('Этот логин уже занят')
    # print('Попробуйте ввести другой')
    # new_user_login = input()
    # if new_user_login not exists in BD:
    # break
    print('Ваш новый логин - ', new_user_login)
    print('Самое время придумать пароль! Он должен содержать более 8 символов.')
    new_user_password = input('Введи свой новый пароль: ')
    while len(new_user_password) <= 8:
        print('Пароль должен содержать более 8ми символов.')
        new_user_password = input()
        if len(new_user_password) > 8:
            break
    number_of_characters = len(new_user_password)
    print('Подтвердите ваш пароль')
    new_user_password_confirmation = input()
    while new_user_password != new_user_password_confirmation:
        print('Введенные пароли не совпадают. Попробуйте еще раз ввести пароль')
        new_user_password_confirmation = input()
        if new_user_password_confirmation == new_user_password:
            break
    print("Количество символов в вашем новом пароле: ", number_of_characters)
    print('Отлично, вы зарегистрированы.')

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
