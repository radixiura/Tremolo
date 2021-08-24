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

int case5() // completed
{
  using namespace std;
  printf("Что бы вы хотели узнать?\n");
  printf("Язык и технологии, используемые при создании Tremolo - 1\n");
  printf("Гарантии безопасности при работе с Tremolo - 2\n");
  printf("Цели и задачи Tremolo - 3\n");
  printf("Назад - 0\n");
  printf("Введите 1, 2, 3 или 0: ");
  int user_choice5; cin >> user_choice5;
  switch(user_choice5)
  {
    case 1:
      printf("В данный момент есть два клиента Tremolo. Один полностью написан на C++, второй на Python3. Используемая СУДБ - PostgreSQL. Также, используется некоторая скриптовая поддержка Shell. Графический интерфейс программы построен на библиотеке Qt.\n");
      break;
    case 2:
      printf("Вы можете просто не ныть, если не верите в безопасность нашего чата.\n");
      break;
    case 3:
      printf("Специально для урегулирования вражды между компилируемыми и интерпретируемыми языками программирования программа для нашего чата написана на c ++ и python.\n");
      break;
    case 0:
      printf("НАЗАД\n");
      break;
    default:
      printf("Вы ввели что - то странное. Возврат к меню.");
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
