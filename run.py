print('Привет!')
print('Рад видеть тебя.')
answer1 = input('Ты уже имеешь аккаунт?')
if answer1 == 'Да':
    print('Отлично.')
if answer1 == 'Д':
    print('Отлично.')
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
print('Отлично, ты зарегистрирован.')
#Блок отправления данных в БД

print('Выбери, что бы ты хотел сделать?')
print('Написать другу - 1')
print('Узнать курс BTC - 2')
print('Узнать свой ip - адрес - 3')
print('Узнать свои настройки сети - 4')
print('Завершить работу - 5')
print('Связаться с разработчиком - 0')

user_choice = input()
if user_choice == 1:
    print(Введи логин )
