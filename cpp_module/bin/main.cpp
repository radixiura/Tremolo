#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include "functions.h"

//#include "user.hpp"
//#include "already_existing_user.hpp"


int main()
{
  using namespace std;
  setlocale(LC_ALL, "Russian");
  int user_answer = get_user_answer();
  switch(user_answer)
  {
  	case 0:
  		new_user_registration();
  		user_authentication();
  		main_menu();
  		break;
  	case 1:
  		user_authentication();
  		main_menu();
  		break;
  	default:
  		printf("Ошибка. Вы ввели что - то странное.");
  		break;
  }
  main_menu();
  return 0;
}
