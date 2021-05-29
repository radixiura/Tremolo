#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <ctime>

//Классы, используемые в программе:

class User
{
  public:
    std::string user_login;
    std::string user_password;
};

class Already_existing_users
{
  public:
    std::string already_existing_user_login;
    std::string already_existing_user_password;
};

//Функции, используемые в программе:

//Функции выбора пользователя из меню:

int case1()
{
  using namespace std;
  printf("Введите логин, на который нужно отправить сообщение: ");
  string login_to_message; cin >> login_to_message;
  return 0;
}

int case2()
{
  //api
  return 0;
}

int case3()
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

int case5()
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
      printf("В данный момент есть два клиента Tremolo. Один полностью написан на C++, второй на Python3.\n");
      break;
    case 2:
      printf("Вы можете просто не ныть, если не верите в безопасность нашего чата.\n");
      break;
    case 3:
      printf("Основной задачей Tremolo является скорейший гешефт.\n");
      break;
    case 0:
      printf("НАЗАД\n");
      break;
  }
  return 0;
}

int case6()
{
  //std::cout << "До свидания, " << User.chel.user_login << "!";
  exit(1);
}

//Функции регистрации и авторизации:

int new_user_registration()
{
  using namespace std;
  string new_user_login; cin >> new_user_login;
  cout << "Ваш новый логин - " << new_user_login << endl;
  printf("Самое время придумать пароль! Он должен быть на английском и содержать более 8ми символов.: ");
  string new_user_password; cin >> new_user_password;
  printf("Введите ваш новый пароль еще раз: ");
  string new_user_password_confirmation; cin >> new_user_password_confirmation;
  while (new_user_password != new_user_password_confirmation)
  {
    printf("Введенные пароли не сходятся. Попробуйте еще раз.\n");
    cout << "Введите пароль: "; cin >> new_user_password_confirmation;
  }
  cout << "Количество символов в вашем пароле: " << sizeof(new_user_password) << endl;
  User chel {new_user_login, new_user_password};
  return 0; 
}

int old_user_authentication()
{
  using namespace std;
  string old_user_login; cin >> old_user_login;
  cout << "Ваш логин - " << old_user_login << endl;
  cout << "Введите пароль: ";
  string old_user_password; cin >> old_user_password;
  User chel {old_user_login, old_user_password};
  return 0;
}

int greeting()
{
  using namespace std;
  printf("Привет!\n");
  printf("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ");
  int user_answer; cin >> user_answer;
  switch(user_answer)
  {
  case 1:
    printf("Введите свой логин: ");
    old_user_authentication();
    break;
  case 0:
    printf("Самое время зарегистрироваться. Введите ваш новый логин: ");
    new_user_registration();
    break;
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
  int user_choice_from_main_menu;
  cin >> user_choice_from_main_menu;
  switch(user_choice_from_main_menu)
  {
    case 1:
      case1();
      break;
    case 2:
      case2();
      break;
    case 3:
      case4();
      break;
    case 4:
      case4();
      break;
    case 5:
      case5();
      break;
    case 6:
      case6();
      break;
  }
  main_menu();
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
