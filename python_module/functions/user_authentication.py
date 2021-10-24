from functions.sub_functions import s_functions


def user_authentication():
    login = s_functions.get_login()
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')
    user_password = input("Введите ваш пароль: ")
    if len(user_password) > 8:
        password = s_functions.get_password()
        print(f"{password}, вы успешно вошли.")
    # if old_user_password exist in DB:
    #   pass
    # else:
    #   print('Пароль введен неверно. Попробуете ввести пароль еще раз?: ')
