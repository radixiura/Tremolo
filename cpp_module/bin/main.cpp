#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
#include <stdlib.h>

#include "user.hpp"
#include "already_existing_user.hpp"

std::string login;
std::string password;

//Функции, используемые в программе:

//Функции выбора пользователя из меню:

int case1() 
{
  using namespace std;
  printf("Введите логин, на который нужно отправить сообщение: ");
  string login_to_message; cin >> login_to_message;
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
      {
      string password_confirmation; cin >> password_confirmation;
      //while(password_confirmation != User.chel.user_password)
      {
        printf("Введенный пароль не соответствует вашему. Попробуйте еще раз.\n");
        cout << "Введите пароль: "; cin >> password_confirmation;
      }
      //printf("Введите ваш новый логин: "); cin >> User.chel.user_login;
      printf("Логин успешно изменен!");
      }
      break;
    case 2:
      printf("Для продолжения введите ваш пароль: ");
      {
      string password_confirmation; cin >> password_confirmation;
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
      string password_confirmation; cin >> password_confirmation;
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

//Функции регистрации и авторизации:

int new_user_registration()
{
  using namespace std;
  printf("Самое время зарегистрироваться. Введите свой новый логин: ");
  string new_user_login; cin >> new_user_login;
  // if new_user_login exists in DB
  // Try again
  cout << "Ваш новый логин: " << new_user_login << endl;
  printf("Самое время придумать пароль. Он должен содержать более 8ми символов: ");
  string new_user_password; cin >> new_user_password;
  printf("Введите свой новый пароль еще раз: ");
  string new_user_password_confirmation; cin >> new_user_password_confirmation;
  while (new_user_password != new_user_password_confirmation)
  {
    printf("Введенные пароли не сходятся. Попробуйте еще раз.\n");
    cout << "Введите пароль: "; cin >> new_user_password_confirmation;
  }
  User chel {new_user_login, new_user_password};
  return 0; 
}

int old_user_authentication()
{
  using namespace std;
  printf("Введите свой логин: ");
  string old_user_login; cin >> old_user_login;
  cout << "Ваш логин - " << old_user_login << endl;
  printf("Введите свой пароль: ");
  string old_user_password; cin >> old_user_password;
  User chel {old_user_login, old_user_password};
  return 0;
}

int greeting()
{
  using namespace std;
  printf("Привет!\n");
  printf("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ");
  static int user_answer; cin >> user_answer;
  switch(user_answer)
  {
  case 1:
    old_user_authentication();
    break;
  case 0:
    new_user_registration();
    break;
  default:
    printf("Вы ввели что - то странное. Попробуйте заново.");
    greeting();
  }
  return 0;
}

//Функции основные:

int main_menu()
{
  using namespace std;
  printf("Меню:\n");
  printf("Отправить сообщение - 1\n");
  printf("Узнать курс BTC - 2\n");
  printf("Узнать свой ip - адрес - 3\n");
  printf("Настройки аккаунта - 4\n");
  printf("Узнать больше о программе - 5\n");
  printf("Завершить работу - 6\n");
  printf("Связаться с разработчиком - 0\n");
  printf("Введите 1, 2, 3, 4, 5, 6 или 0: ");
  int user_choice_from_main_menu; cin >> user_choice_from_main_menu;
  switch(user_choice_from_main_menu)
  {
    case 1:
      case1();
      main_menu();
      break;
    case 2:
      case2();
      main_menu();
      break;
    case 3:
      case4();
      main_menu();
      break;
    case 4:
      case4();
      main_menu();
      break;
    case 5:
      case5();
      main_menu();
      break;
    case 6:
      case6();
      main_menu();
      break;
    case 0:
      case0();
      main_menu();
      break;
    default:
      printf("Вы ввели что - то странное. Возврат к меню.");
      main_menu();
      break;
  }
  return 0;
}

int main()
{
  using namespace std;
  setlocale(LC_ALL, "Russian");
  greeting();
  main_menu();
  return 0;
}


// Доработки:
// 1. При введении не цифры в строке 195, происходит кринж
// 2. Настроить проверку правильности пароля в case4
// 3. Подключить python-модули для case2 и case3
// 4. Сделать графический интерфейс
// 5. 
