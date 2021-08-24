#ifndef NEW_USER_REGISTRATION_H
#define NEW_USER_REGISTRATION_H

// Регистрация нового пользователя

int new_user_registration()
{
  using namespace std;
  printf("Самое время зарегистрироваться. Введите свой новый логин: ");
  char new_user_login[10]; cin >> new_user_login;
  // if new_user_login exists in DB
  // Try again
  cout << "Ваш новый логин: " << new_user_login << endl;
  printf("Самое время придумать пароль. Он должен содержать более 8ми символов: ");
  char new_user_password[24]; cin >> new_user_password;
  printf("Введите свой новый пароль еще раз: ");
  char new_user_password_confirmation[24]; cin >> new_user_password_confirmation;
  while (new_user_password != new_user_password_confirmation)
  {
    printf("Введенные пароли не сходятся. Попробуйте еще раз.\n");
    cout << "Введите пароль: "; cin >> new_user_password_confirmation;
  }
  return 0; 
}

#endif
