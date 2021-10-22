def new_user_registration():
    
    new_user_login = input("Самое время зарегистрироваться. Введите свой новый логин:  ")
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
    print("Самое время придумать пароль. Он должен содержать более 8ми символов: ")
    new_user_password = input("Введите ваш новый пароль: ")
    while len(new_user_password) < 8:
        print('Пароль должен содержать более 8ми символов. Попробуйте заново.')
        new_user_password = input()
        if len(new_user_password) > 8:
            break
    new_user_password_confirmation = input("Введите свой новый пароль еще раз: ")
    while new_user_password != new_user_password_confirmation:
        print('Введенные пароли не сходятся. Попробуйте еще раз.\n')
        new_user_password_confirmation = input()
        if new_user_password_confirmation == new_user_password:
            break
    return new_user_login
    
