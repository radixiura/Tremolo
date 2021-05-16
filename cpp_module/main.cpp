#include <iostream>
#include <cstdio>
#include <string>

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
  string new_user_password;
  cout << "Самое время придумать пароль! Он должен быть на английском и содержать более 8ми символов.: ";
  cin >> new_user_password;
  cout << "Количество символов в вашем пароле: " << new_user_password.length() << endl;
  return 0; 
}

int main_menu()
{
  printf("Меню:\n");
  printf("Отправить сообщение - 1\n");
  printf("Узнать курс BTC - 2\n");
  printf("Узнать свой ip - адрес - 3\n");
  printf("Настройки аккаунта - 4\n");
  printf("Узнать больше о программе - 5\n");
  printf("Завершить работу - 6\n");
  printf("Связаться с разработчиком - 0\n");
  return 0;
}

int main()
{
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

  return 0;
}
