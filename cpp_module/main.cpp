#include <iostream>
#include <cstdio>
#include <cstring>

//Классы, используемые в программе.

struct User
{
  char login[256];
  char password[256];
  char keyword[256];
};

//Функции, используемые в программе.

int greeting()
{
  printf("Привет.\n");
  printf("Рад видеть тебя.\n");
  return 0;
}

int old_user_authentication()
{
  using namespace std;
  string old_user_login;
  cin >> old_user_login;
  cout << "Ваш логин - " << old_user_login << endl;
  string old_user_password;
  cout << "Введите пароль: ";
  cin >> old_user_password;
  return 0;
}

int new_user_registration()
{
  using namespace std;
  string new_user_login;
  cin >> new_user_login;
  cout << "Ваш логин - " << new_user_login << endl;
  cout << "Самое время придумать пароль! Он должен быть на английском и содержать более 8ми символов.: ";
  string new_user_password;
  cin >> new_user_password;
  printf("Введите ваш новый пароль еще раз: ");
  string new_user_password_confirmation;
  cin >> new_user_password_confirmation;
  while (new_user_password != new_user_password_confirmation)
  {
    printf("Введенные пароли не сходятся. Попробуйте еще раз.\n");
    printf("Введите ваш новый пароль еще раз: ");
    cin >> new_user_password_confirmation;
  }
  cout << "Количество символов в вашем пароле: " << sizeof(new_user_password) << endl;
  return 0; 
}

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
  int user_choice5;
  cin >> user_choice5;
  switch(user_choice5)
  {
    case 1:
      printf("В данный момент есть два клиента Tremolo. Один полностью написан на C++, второй на Python3.\n");
      break;
    case 2:
      printf("Вы можете просто отсосать мой член, если не верите в безопасность нашего чата.\n");
      break;
    case 3:
      printf("Основной задачей Tremolo является скорейшая продажа этой хуйни и последующий гешефт.\n");
      break;
    case 0:
      printf("НАЗАД БЛЯДЬ.\n");
      break;
  }
  return 0;
}

int templatemo()
{
  using namespace std;
  int user_choice_from_main_menu;
  cin >> user_choice_from_main_menu;
  switch(user_choice_from_main_menu)
  {
    case 1:
      printf("lalala");
      //функция
    case 2:
      printf("Отчет по курсу BTC к валютам.\n");
      //api
      break;
    case 3:
      printf("Ваш текущий ip-адрес");
      //api
      break;
    case 4:
      printf("Что бы вы хотели настроить?");
    case 5:
      case5();
    case 6:
      printf("До свидания!");
      //Выход
      break;
  }
  return 0;
}

int user_answer_from_main_menu()
{
  using namespace std;
  templatemo();
  return 0;
}

int main()
{
  setlocale(LC_ALL, "Russian");
  using namespace std;
  greeting();
  cout << "Ты уже имеешь аккаунт? Введи 1 если да, 0 если нет: ";
  int user_answer;
  cin >> user_answer;
  switch(user_answer)
  {
  case 1:
    printf("Введите свой логин: ");
    old_user_authentication();
    break;
  case 0:
    printf("Самое время зарегистрироваться. Введите свой новый логин: ");
    new_user_registration();
    break;
  default:
    printf("Введи 1 или 0.");
    break;
  }
  main_menu();
  user_answer_from_main_menu();
  return 0;
}
