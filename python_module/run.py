def menu():
    print('Выбери, что бы ты хотел сделать?')
    print('Отправить сообщение - 1')
    print('Узнать курс BTC - 2')
    print('Узнать свой ip - адрес - 3')
    print('Узнать свои настройки сети - 4')
    print('Завершить работу - 5')
    print('Связаться с разработчиком - 0')

def greeting():
    print("Привет.")
    print("Рад видеть тебя.")

greeting()

answer1 = input('Ты уже имеешь аккаунт?: ')

if answer1 == 'Да':
    print('Отлично.')
    old_user_login = input("Введите ваш логин: ")
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')
    print('Ваш логин - ' + old_user_login)
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
    print('Самое время придумать пароль! Рекомендуем использовать пароль, состоящий более чем из 8ми символов.')
    new_user_password = input('Введи свой новый пароль')
    number_of_characters = len(new_user_password)
    print("Количество символов в вашем новом пароле: ", number_of_characters)
    print('Подтвердите ваш пароль')
    new_user_password_confirmation = input()
    while new_user_password != new_user_password_confirmation:
        print('Введенные пароли не совпадают. Попробуйте еще раз ввести пароль')
        new_user_password_confirmation = input()
        if new_user_password_confirmation == new_user_password:
            break
    print('Отлично, ты зарегистрирован.')

menu()

user_choice = input()

if user_choice == 1:
    print('Введи логин своего знакомого')
    new_request = input()
    # if new_request exists in BD and everything is ok:
    # print('Соединение успешно установлено.')
    # Начало переписки
    # if new_request not exists in BD:
    # print('Данный логин не найден.')
elif user_choice == 2:
    print('Актуальный курс биткоина')
    # api
elif user_choice == 3:
    print("Ваш текущий ip-адрес")
    # api
elif user_choice == 4:
    print('Ваши текущие настройки сети')
    # api
elif user_choice == 5:
    print('До свидания!')
    exit()
elif user_choice == 0:
    print('Реще')
    # api
