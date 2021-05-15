import requests
import bs4
def menu():
    print('Меню:')
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
    new_user_password = input('Введи свой новый пароль: ')
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

user_choice = input("Выберите действие: ")

if user_choice == "1":
    print('Введи логин своего знакомого')
    # if new_request exists in BD and everything is ok:
    # print('Соединение успешно установлено.')
    # Начало переписки
    # if new_request not exists in BD:
    # print('Данный логин не найден.')
elif user_choice == "2":
    response = requests.get('https://apirone.com/api/v2/ticker?currency=btc')
    if response:
        print('Отчет по курсу BTC к валютам готов.')
    else:
        print('Произошла ошибка.')
    print(response.text)
elif user_choice == "3":
    print("Ваш текущий ip-адрес")
    s = requests.get('https://2ip.ua/ru/')
    b = bs4.BeautifulSoup(s.text, "html.parser")
    a = b.select(" .ipblockgradient .ip")[0].getText()
    print(a)
elif user_choice == "4":
    print('Ваши текущие настройки сети')
    # api
elif user_choice == "5":
    print('До свидания!')
    exit()
elif user_choice == "0":
    print('Значит, ты выбрал смерть...')

