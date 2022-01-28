#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <string>
#include "functions_principale.h"
#include "new_user_registration.h"
#include "user_authentication.h"
#include "menu_principale.h"

//#include "user.hpp"
//#include "already_existing_user.hpp"


int main()
{
  using namespace std;
  setlocale(LC_ALL, "Russian");
  int user_answer = greetings();
  switch(user_answer)
  {
  	case 0:
  		new_user_registration();
  		break;
  	case 1:
  		break;
  	default:
  		printf("Ошибка. Вы ввели что - то странное.\n");
  		break;
  }
  user_authentication();
  main_menu_buttons();
  return 0;
}
