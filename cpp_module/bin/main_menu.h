#ifndef MAIN_MENU_H
#define MAIN_MENU_H

using namespace std;

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
  printf("Введите 1, 2, 3, 4, 5, 6 или 0: ");
  int user_choice_from_main_menu; cin >> user_choice_from_main_menu;
  switch(user_choice_from_main_menu)
  {
    case 1:
  		printf("Введите логин, на который нужно отправить сообщение: ");
  		char login_to_message; cin >> login_to_message;
  		// if login_to_message exists in DB
  		//...
  		// Try again
    	main_menu();
    case 2:
        //api
        main_menu();
    case 3:
      	//api
      	main_menu();
    case 4:
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
  				
  		}
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

#endif
