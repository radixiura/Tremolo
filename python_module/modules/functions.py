import requests
import bs4

def greeting():
    print("Привет.")
    print("Рад видеть тебя.")
    
def main_menu():
    print("Меню:")
    print("Отправить сообщение - 1")
    print("Узнать курс BTC - 2")
    print("Узнать свой ip - адрес - 3")
    print("Настройки аккаунта - 4")
    print("Узнать больше о программе - 5")
    print("Завершить работу - 6")
    print("Связаться с разработчиком - 0")
    
def menu1():
    print("lalala")
    
def menu2():
    response = requests.get('https://apirone.com/api/v2/ticker?currency=btc')
    if response:
        print('Отчет по курсу BTC к валютам готов.')
    else:
        print('Произошла ошибка.')
    print(response.text)
    
def menu3():
    print("Ваш текущий ip-адрес")
    pepsi = requests.get('https://2ip.ua/ru/')
    sprite = bs4.BeautifulSoup(pepsi.text, "html.parser")
    ip_address_info = sprite.select(" .ipblockgradient .ip")[0].getText()
    print(ip_address_info)
    
def menu4():
    print("Что бы вы хотели настроить?")
    
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
        print("Вы можете просто отсосать мой член, если не верите в безопасность нашего чата.")
    elif user_choice5 == "3":
        print("Основной задачей Tremolo является скорейшая продажа этой хуйни и последующий гешефт.")
    elif user_choice5 == "4":
        print("НАЗАД БЛЯДЬ")
        
def menu6():
    print('До свидания!')
    exit()
