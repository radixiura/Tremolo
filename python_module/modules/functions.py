import sys
import requests
import bs4


#  Menu functions


def main_menu_modules_1():
    login_for_new_message = input("Введите логин, на который нужно отправить сообщение: ")
    message = input(f"Введите сообщение для {login_for_new_message}: ")
    print(message)
    # if login_for_new_message exists in DB
    #   new_message = input("Введите текст вашего сообщения: ")
    # elif login_for_new_message not exists in DB
    #   print("Введенного логина не существует в нашей базе данных!)
    # else:
    #   print("Произошла ошибка")
    # print(f"Введите сообщение для {login_for_message} : ")


def main_menu_modules2():
    response = requests.get('https://apirone.com/api/v2/ticker?currency=btc')
    if response:
        print('Отчет по курсу BTC к валютам готов.')
    else:
        print('Произошла ошибка.')
    print(response.text)
    main_menu()


def main_menu_modules3():
    print("Ваш текущий ip-адрес")
    pepsi = requests.get('https://2ip.ua/ru/')
    sprite = bs4.BeautifulSoup(pepsi.text, "html.parser")
    ip_address_info = sprite.select(" .ipblockgradient .ip")[0].getText()
    print(ip_address_info)
    main_menu()


def main_menu_modules4():
    print("Что бы вы хотели настроить?")
    print("Изменить логин - 1")
    print("Изменить пароль - 2")
    print("Изменить аватар - 3")
    print("Удалить аккаунт - 4")
    print("Назад - 0")
    user_choice4 = input("Выберите действие: ")
    if user_choice4 == "1":
        password_confirmation = input("Для продолжения введите ваш пароль: ")
        global password
        while password_confirmation != password:
            print("Не слишком похоже на ваш пароль. Попробуйте заново.")
            password_confirmation = input()
            if password_confirmation == password:
                login = input("Введите ваш новый логин:")
                print(f"Ваш новый логин - {login} !")
                break
    elif user_choice4 == "2":
        password_confirmation = input("Для продолжения введите ваш пароль: ")
    elif user_choice4 == "3":
        print("Вставьте ссылку на ваш новый аватар: ")
    elif user_choice4 == "4":
        password_confirmation = input("Для продолжения введите ваш пароль: ")
        print("Ваш аккаунт удален. До свидания!")
        exit()
        main_menu()


def main_menu_modules5():
    print("Что бы вы хотели узнать?")
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


def main_menu_modules6():
    print("До свидания")
    exit()


def main_menu_modules0():
    print("В настоящий момент я хикканю и у меня нет желания говорить.")


def new_user_registration():
    print("Самое время придумать логин.")
    print("Он должен содержать более 8ми символов.")
    new_user_login = input("Введите ваш новый логин: ")
    while len(new_user_login) < 8:
        print('Логин должен содержать более 8ми символов. Попробуйте заново.')
        new_user_login = input()
        if len(new_user_login) > 8:
            break
    # while new_user_login exists in BD
    # print('Этот логин уже занят')
    # print('Попробуйте ввести другой')
    # new_user_login = input()
    # if new_user_login not exists in BD:
    # break
    print(f"Ваш новый логин: {new_user_login}")
    print("Самое время придумать пароль. Он должен содержать более 8ми символов.")
    new_user_password = input("Введите ваш новый пароль: ")
    while len(new_user_password) < 8:
        print('Пароль должен содержать более 8ми символов. Попробуйте заново.')
        new_user_password = input()
        if len(new_user_password) > 8:
            break
    new_user_password_confirmation = input("Подтвердите ваш пароль: ")
    while new_user_password != new_user_password_confirmation:
        print('Введенные пароли не совпадают. Попробуйте еще раз ввести пароль')
        new_user_password_confirmation = input()
        if new_user_password_confirmation == new_user_password:
            break
    return new_user_login


def get_old_login():
    old_login = input("Введите свой логин: ")
    return old_login


def get_old_password():
    old_password = input("Введите свой пароль: ")
    return old_password


def old_user_authentication():
    old_user_login = input("Введите ваш логин: ")
    print(f"Ваш логин: {old_user_login}")
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')
    old_user_password = input("Введите ваш пароль: ")
    if len(old_user_password) > 8:
        print(f"{old_user_login}, вы успешно вошли.")
    # if old_user_password exist in DB:
    #   pass
    # else:
    #   print('Пароль введен неверно. Попробуете ввести пароль еще раз?: ')


#  Menu functions


def main_menu():
    print("Меню:")
    print("Отправить сообщение - 1")
    print("Узнать курс BTC - 2")  # ready
    print("Узнать свой ip - адрес - 3")  # ready
    print("Настройки аккаунта - 4")
    print("Узнать больше о программе - 5")  # ready
    print("Завершить работу - 6")  # ready
    print("Связаться с разработчиком - 0")
    user_choice = input("Выберите действие: ")
    if user_choice == "1":
        main_menu_modules_1()
    elif user_choice == "2":
        main_menu_modules2()
    elif user_choice == "3":
        main_menu_modules3()
    elif user_choice == "4":
        main_menu_modules4()
    elif user_choice == "5":
        main_menu_modules5()
    elif user_choice == "6":
        main_menu_modules6()
    elif user_choice == "0":
        main_menu_modules0()
