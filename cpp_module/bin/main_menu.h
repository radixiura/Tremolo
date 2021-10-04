#ifndef MENU_FUNCTIONS_H
#define MENU_FUNCTIONS_H

int case1() 
{
  using namespace std;
  printf("Введите логин, на который нужно отправить сообщение: ");
  char login_to_message; cin >> login_to_message;
  // if login_to_message exists in DB
  // Try again
  return 0;
}

int case2() // almost completed
{
  //api
  return 0;
}

int case3() // almost completed
{
  //api
  return 0;
}

int case4()
{
  using namespace std;
  printf("Что бы вы хотели настроить?\n");
  printf("Изменить логин - 1\n");
  printf("Изменить пароль - 2\n");
  printf("Изменить аватар - 3\n");
  printf("Удалить аккаунт - 4\n");
  printf("Назад - 0\n");
  printf("Введите 1, 2, 3, 4 или 0: ");
  int user_choice4; cin >> user_choice4;
  switch(user_choice4)
  {
    case 1:
      printf("Для продолжения введите ваш пароль: ");
      char password_confirmation; cin >> password_confirmation;
      //while(password_confirmation != пароль, введенный пользователем)
      {
        printf("Введенный пароль не соответствует вашему. Попробуйте еще раз.\n");
        cout << "Введите пароль: "; cin >> password_confirmation;
      }
      //printf("Введите ваш новый логин: "); cin >> переменная, в которой хранится логин;
      printf("Логин успешно изменен!");
      break;
    case 2:
      printf("Для продолжения введите ваш пароль: ");
      {
      char password_confirmation; cin >> password_confirmation;
      //while(password_confirmation != User.chel.user_password)
      {
        printf("Введенный пароль не соответствует вашему. Попробуйте еще раз.\n");
        cout << "Введите пароль: "; cin >> password_confirmation;
      }
      //printf("Введите ваш новый пароль: "); cin >> User.chel.user_password;
      printf("Пароль успешно изменен!");
      }
      break;
    case 3:
      printf("Вставьте ссылку на ваш новый аватар");
      break;
    case 4:
      printf("Для продолжения введите ваш пароль: ");
      {
      char password_confirmation; cin >> password_confirmation;
      //while(password_confirmation != User.chel.user_password)
      {
        printf("Введенный пароль не соответствует вашему. Попробуйте еще раз.\n");
        cout << "Введите пароль: "; cin >> password_confirmation;
      }
      printf("Ваш аккаунт удален. До свидания!");
      exit(1);
      }
      break;
  }
  return 0;
}

int case6() // almost completed
{
  //std::cout << "До свидания, " << User.chel.user_login << "!";
  exit(1);
}

int case0() // completed
{
  printf("В настоящий момент я хикканю и у меня нет желания говорить.\n");
  return 0;
}

#endif
