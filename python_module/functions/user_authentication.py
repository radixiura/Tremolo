def user_authentication():
    login = input("Введите ваш логин: ")
    # if old_user_login exist in DB:
    #   pass
    # else:
    #   print('Данный логин не найден в базе данных. Попробуете ввести логин еще раз?: ')
    password = input("Введите ваш пароль: ")
    print(f"{login}, вы успешно вошли.")
    # if old_user_password exist in DB:
    #   pass
    # else:
    #   print('Пароль введен неверно. Попробуете ввести пароль еще раз?: ')
    return login, password
