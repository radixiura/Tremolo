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
  setlocale(LC_ALL, "Russian");
  greeting();
  cout << "Ты уже имеешь аккаунт?: ";
  string user_answer;
  cin >> user_answer;

  main_menu();

  return 0;
}
