#include <stdio.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <climits>
#include <ctime>
#include <stdlib.h>
#include "functions.h"

//#include "user.hpp"
//#include "already_existing_user.hpp"


int get_user_answer()
{
	while (true)
	{
		printf("Привет!\n");
		printf("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ");
		int user_answer; cin >> user_answer;
		if (user_answer == 1 || user_answer == 0)
			return user_answer;
		else
			printf("siegout");
	}
}


void log_in_choice(int get_user_answer)
{
	if (get_user_answer == '1')
		old_user_authentication();
	if (get_user_answer == '0')
		new_user_registration();
}


int main()
{
  using namespace std;
  setlocale(LC_ALL, "Russian");
  int user_answer = get_user_answer();
  while (get_user_answer() != 1 && 0)
  {
  	printf("Высад");
  }
  switch(user_answer)
  {
  	case 0:
  		new_user_registration();
  		main_menu();
  		break;
  	case 1:
  		old_user_authentication();
  		main_menu();
  		break;
  	default:
  		printf("dichka");
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
