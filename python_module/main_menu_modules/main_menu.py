import requests
import bs4


def main_menu_buttons():
    print("Меню:")
    print("Отправить сообщение - 1")
    print("Узнать курс BTC - 2")  # ready
    print("Узнать свой ip - адрес - 3")  # ready
    print("Настройки аккаунта - 4")
    print("Узнать больше о программе - 5")  # ready
    print("Завершить работу - 6")  # ready
    print("Связаться с разработчиком - 0")
    user_choice = input("Введите 1, 2, 3, 4, 5, 6 или 0: ")
    if user_choice == "1":
        main_menu_modules_1()
    elif user_choice == "2":
        main_menu_modules_2()
    elif user_choice == "3":
        main_menu_modules_3()
    elif user_choice == "4":
        main_menu_modules_4()
    elif user_choice == "5":
        main_menu_modules_5()
    elif user_choice == "6":
        main_menu_modules_6()
    elif user_choice == "0":
        main_menu_modules_0()
        
        
def main_menu_modules_1():
    login_for_new_message = input("Введите логин, на который нужно отправить сообщение: ")
    message = input(f"Введите сообщение для {login_for_new_message}: ")
    print(message)
    main_menu_buttons()
    # if login_for_new_message exists in DB
    #   new_message = input("Введите текст вашего сообщения: ")
    # elif login_for_new_message not exists in DB
    #   print("Введенного логина не существует в нашей базе данных!)
    # else:
    #   print("Произошла ошибка")
    # print(f"Введите сообщение для {login_for_message} : ")


def main_menu_modules_2():
    response = requests.get('https://apirone.com/api/v2/ticker?currency=btc')
    if response:
        print('Курс BTC:')
    else:
        print('Произошла ошибка.')
    print(response.text)
    main_menu_buttons()


def main_menu_modules_3():
    print("Текущий IP - адрес: ")
    pepsi = requests.get('https://2ip.ua/ru/')
    sprite = bs4.BeautifulSoup(pepsi.text, "html.parser")
    ip_address_info = sprite.select(" .ipblockgradient .ip")[0].getText()
    print(ip_address_info)
    main_menu_buttons()


def main_menu_modules_4():
    print("Что бы вы хотели настроить?")
    print("Изменить логин - 1")
    print("Изменить пароль - 2")
    print("Изменить аватар - 3")
    print("Удалить аккаунт - 4")
    print("Назад - 0")
    user_choice4 = input("Введите 1, 2, 3, 4 или 0: ")
    if user_choice4 == "1":
        password_confirmation = input("Для продолжения введите ваш пароль: ")
        #while password_confirmation != password:
            #print("Не слишком похоже на ваш пароль. Попробуйте заново.")
            #password_confirmation = input()
            #if password_confirmation == password:
                #login = input("Введите ваш новый логин:")
                #print("Логин успешно изменен!")
                #break
    elif user_choice4 == "2":
        password_confirmation = input("Для продолжения введите ваш пароль: ")
    elif user_choice4 == "3":
        print("Вставьте ссылку на ваш новый аватар")
    elif user_choice4 == "4":
        password_confirmation = input("Для продолжения введите ваш пароль: ")
        print("Ваш аккаунт удален. До свидания!")
        exit()
        main_menu_buttons()


def main_menu_modules_5():
    print("Что бы вы хотели узнать?")
    print('Язык и технологии, используемые при создании Tremolo - 1')
    print('Гарантии безопасности при работе с Tremolo - 2')
    print('Цели и задачи Tremolo - 3')
    print('Назад - 0')
    user_choice5 = input("Введите 1, 2, 3 или 0: ")
    if user_choice5 == "1":
        print("В данный момент есть два клиента Tremolo. Один полностью написан на C++, второй на Python3. Используемая СУДБ - PostgreSQL. Также, используется некоторая скриптовая поддержка Shell. Графический интерфейс программы построен на библиотеке Qt.")
    elif user_choice5 == "2":
        print("Вы можете просто связаться с разработчиком, если не верите в безопасность нашего чата.")
    elif user_choice5 == "3":
        print("Специально для урегулирования вражды между компилируемыми и интерпретируемыми языками программирования программа для нашего чата написана на c ++ и python.\n")
    elif user_choice5 == "3":
        main_menu_buttons()
    elif user_choice5 == "0":
        print("НАЗАД")
    main_menu_buttons()


def main_menu_modules_6():
    print("До свидания")
    exit()


def main_menu_modules_0():
    print("В настоящий момент я хикканю и у меня нет желания говорить.")
