#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
#include <stdlib.h>
#include "constants.h"
#include "functions.h"

//#include "user.hpp"
//#include "already_existing_user.hpp"

int main()
{
  using namespace std;
  setlocale(LC_ALL, "Russian");
  printf("Привет!\n");
  printf("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ");
  int user_answer; cin >> user_answer;
  switch(user_answer)
  {
  	case 0:
  		new_user_registration();
  		break;
  	case 1:
  		old_user_authentication();
  		break;
  }
  main_menu();
  
  return 0;
}



// Доработки:
// 1. При введении не цифры в строке 195, происходит кринж
// 2. Настроить проверку правильности пароля в case4
// 3. Подключить python-модули для case2 и case3
// 4. Сделать графический интерфейс
// 5. 
