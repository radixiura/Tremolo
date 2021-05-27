import requests
import bs4


def greeting():
    print("Привет.")
    print("Рад видеть вас.")


def main_menu():
    print("Меню:")
    print("Отправить сообщение - 1")
    print("Узнать курс BTC - 2")  # ready
    print("Узнать свой ip - адрес - 3")  # ready
    print("Настройки аккаунта - 4")
    print("Узнать больше о программе - 5")  # ready
    print("Завершить работу - 6")  # ready
    print("Связаться с разработчиком - 0")


def old_user_registration():
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


def new_user_registration():
    print("Думаю, вам стоит зарегистрироваться.")
    new_user_login = input("Введите ваш новый логин: ")
    # while new_user_login exists in BD
    # print('Этот логин уже занят')
    # print('Попробуйте ввести другой')
    # new_user_login = input()
    # if new_user_login not exists in BD:
    # break
    print('Ваш новый логин - ', new_user_login)
    print('Самое время придумать пароль! Он должен содержать более 8 символов.')
    new_user_password = input("Введите ваш новый пароль: ")
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


def menu1():
    print("Общение это прекрасно.")
    login_for_new_message = input("Введите логин, на который нужно отправить сообщение: ")
    # if login_for_new_message exists in DB
    #   new_message = input("Введите текст вашего сообщения: ")
    # elif login_for_new_message not exists in DB
    #   print("Введенного логина не существует в нашей базе данных!)
    # else:
    #   print("Произошла ошибка")
    main_menu()


def menu2():
    response = requests.get('https://apirone.com/api/v2/ticker?currency=btc')
    if response:
        print('Отчет по курсу BTC к валютам готов.')
    else:
        print('Произошла ошибка.')
    print(response.text)
    main_menu()


def menu3():
    print("Ваш текущий ip-адрес")
    pepsi = requests.get('https://2ip.ua/ru/')
    sprite = bs4.BeautifulSoup(pepsi.text, "html.parser")
    ip_address_info = sprite.select(" .ipblockgradient .ip")[0].getText()
    print(ip_address_info)
    main_menu()


def menu4():
    print("Что бы вы хотели настроить?")
    main_menu()


def menu5():
    print('Что бы вы хотели узнать?')
    print('Язык и технологии, используемые при создании Tremolo - 1')
    print('Гарантии безопасности при работе с Tremolo - 2')
    print('Цели и задачи Tremolo - 3')
    print('Назад - 0')
    user_choice5 = input("Выберите действие: ")
    if user_choice5 == "1":
        print("В данный момент есть два клиента Tremolo. Один полностью написан на C++, второй на Python3.")
    elif user_choice5 == "2":
        print("Вы можете просто не ныть, если не верите в безопасность нашего чата.")
    elif user_choice5 == "3":
        print("Основной задачей Tremolo является скорейший гешефт.")
        main_menu()
    elif user_choice5 == "0":
        print("НАЗАД")
    main_menu()


def menu6():
    print('До свидания!')
    exit()
