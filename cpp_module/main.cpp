#include <iostream>
#include <cstdio>

struct User
{
  char login[256];
  char password[256];
  char keyword[256];
};

int greeting()
{
  printf("Привет.");
  printf("Рад видеть тебя.");
  return 0;
}

int main()
{
  greeting();
  
  return 0;
}
