def user_authentication():
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
