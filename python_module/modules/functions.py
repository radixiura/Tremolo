import sys
import requests
import bs4
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication)


def greeting():
    print("Привет!")


def old_user_registration():
    old_user_login = input("Введите ваш логин: ")
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')
    old_user_password = input("Введите ваш пароль: ")
    # if old_user_password exist in DB:
    #   pass
    # else:
    #   print('Пароль введен неверно. Попробуете ввести пароль еще раз?: ')
    old_user_password = password
    main_menu()


def new_user_registration():
    new_user_login = input("Самое время зарегистрироваться. Введите свой новый логин: ")
    # while new_user_login exists in BD
    # print('Этот логин уже занят')
    # print('Попробуйте ввести другой')
    # new_user_login = input()
    # if new_user_login not exists in BD:
    # break
    print(f"Ваш новый логин: {new_user_login}")
    print("Самое время придумать пароль. Он должен содержать более 8ми символов.")
    new_user_password = input("Введите ваш новый пароль: ")
    while len(new_user_password) <= 8:
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
    new_user_password = password
    main_menu()


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
        menu1()
    elif user_choice == "2":
        menu2()
    elif user_choice == "3":
        menu3()
    elif user_choice == "4":
        menu4()
    elif user_choice == "5":
        menu5()
    elif user_choice == "6":
        menu6()
    elif user_choice == "0":
        print('Значит, ты выбрал смерть...')


def menu1():
    print("Общение это прекрасно.")
    login_for_new_message = input("Введите логин, на который нужно отправить сообщение: ")
    send_message()
    # if login_for_new_message exists in DB
    #   new_message = input("Введите текст вашего сообщения: ")
    # elif login_for_new_message not exists in DB
    #   print("Введенного логина не существует в нашей базе данных!)
    # else:
    #   print("Произошла ошибка")
    main_menu()


def send_message():
    class Example(QWidget):

        def __init__(self):
            super().__init__()

            self.initUI()

        def initUI(self):
            receiver = QLabel('Title')
            theme = QLabel('Author')
            message = QLabel('Review')

            title_edit = QLineEdit()
            author_edit = QLineEdit()
            review_edit = QTextEdit()

            grid = QGridLayout()
            grid.setSpacing(10)

            grid.addWidget(receiver, 1, 0)
            grid.addWidget(title_edit, 1, 1)

            grid.addWidget(theme, 2, 0)
            grid.addWidget(author_edit, 2, 1)

            grid.addWidget(message, 3, 0)
            grid.addWidget(review_edit, 3, 1, 5, 1)

            self.setLayout(grid)

            self.setGeometry(300, 300, 350, 300)
            self.setWindowTitle('Review')
            self.show()

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        ex = Example()
        sys.exit(app.exec_())


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


def menu5():
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


def menu6():
    print('До свидания!')
    exit()
