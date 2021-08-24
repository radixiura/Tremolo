#ifndef OLD_USER_AUTHENTICATION_H
#define OLD_USER_AUTHENTICATION_H

// Аутентификация старого пользователя

int old_user_authentication()
{
  using namespace std;
  printf("Введите свой логин: ");
  char old_user_login[10]; cin >> old_user_login;
  cout << "Ваш логин - " << old_user_login << endl;
  printf("Введите свой пароль: ");
  char old_user_password[24]; cin >> old_user_password;
  return 0;
}

#endif
