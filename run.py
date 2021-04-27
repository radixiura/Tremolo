import os
import sys
print('Привет!')
print('Рад видеть тебя.')
answer1 = input('Ты уже имеешь аккаунт?')
if answer1 == 'Да' or 'да' or 'Д' or 'д' or 'Y' or 'y':
    print('Отлично.')
    def menu():
        print('Выбери, что бы ты хотел сделать?')
        print('Написать другу - 1')
        print('Узнать курс BTC - 2')
        print('Узнать свой ip - адрес - 3')
        print('Узнать свои настройки сети - 4')
        print('Завершить работу - 5')
        print('Связаться с разработчиком - 0')
    p = menu()
else:
    print('Думаю, тебе стоит зарегистрироваться.')
    new_user_login = input('Введи свой новый логин')
    #while new_user_login exists in BD
        #print('Этот логин уже занят')
        #print('Попробуйте ввести другой')
        #new_user_login = input()
        #if new_user_login not exists in BD:
            #break
    print('Ваш новый логин - ', new_user_login)
    print('Самое время придумать пароль!')
    new_user_password = input('Введи свой новый пароль')
    print('Подтвердите ваш пароль')
    new_user_password_confirmation = input()
    while new_user_password != new_user_password_confirmation:
        print('Введенные пароли не совпадают. Попробуйте еще раз ввести пароль')
        new_user_password_confirmation = input()
        if new_user_password_confirmation == new_user_password:
            break
            continue
print('Отлично, ты зарегистрирован.')
def menu():
    print('Выбери, что бы ты хотел сделать?')
    print('Написать другу - 1')
    print('Узнать курс BTC - 2')
    print('Узнать свой ip - адрес - 3')
    print('Узнать свои настройки сети - 4')
    print('Завершить работу - 5')
    print('Связаться с разработчиком - 0')
#Блок отправления данных в БД

user_choice = input("Введи желаемое")
if user_choice == 1:
    print('Введи логин своего знакомого')
    new_request = input()
    #if new_request exists in BD and everything is ok:
        #print('Соединение успешно установлено.')
    #Начало переписки
    #if new_request not exists in BD:
        #print('Данный логин не найден.')
elif user_choice == 2:
    print('Актуальный курс биткоина')
    #api
elif user_choice == 3:
    print("Ваш текущий ip-адрес")
    #api
elif user_choice == 4:
    print('Ваши текущие настройки сети')
    #api
elif user_choice == 5:
    print('До свидания!')
    exit()
elif user_choice == 0:
    print('Реще')
    #api
