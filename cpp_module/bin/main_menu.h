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
      		printf("В данный момент есть два клиента Tremolo. Один полностью написан на C++, второй на Python3. Используемая СУДБ - PostgreSQL. Также, используется некоторая скриптовая поддержка Shell. Графический интерфейс программы построен на библиотеке Qt.\n");
      		break;
    	case 2:
      		printf("Вы можете просто не ныть, если не верите в безопасность нашего чата.\n");
      		break;
    	case 3:
      		printf("Специально для урегулирования вражды между компилируемыми и интерпретируемыми языками программирования программа для нашего чата написана на c ++ и python.\n");
      		break;
    	case 0:
      		printf("НАЗАД\n");
      		break;
    	default:
      		printf("Вы ввели что - то странное. Возврат к меню.");
      		break;
  		}
      	main_menu();
    case 6:
     {
     	//std::cout << "До свидания, " << User.chel.user_login << "!";
     	exit(1);
     }
    case 0:
	{
  		printf("В настоящий момент я хикканю и у меня нет желания говорить.\n");
  		main_menu();
	}
    default:
      printf("Вы ввели что - то странное. Возврат к меню.");
      main_menu();
      break;
  }
  return 0;
}

#endif
