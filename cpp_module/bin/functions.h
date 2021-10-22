#ifndef FUNCTIONS_H
#define FUNCTIONS_H
                                                                                                                                       

using namespace std;


//  Menu functions


int main_menu_modules_1()
{
	printf("Введите логин, на который нужно отправить сообщение: ");
	string login_to_message; getline(cin, login_to_message);
	// Проверка существования логина
	cout << "Введите сообщения для " << login_to_message << ":" << endl;
	string message; getline(cin, message);
	cout << message;
	// Отправка сообщения
	return 0;
}


int main_menu_modules_2()
{
	printf("Курс BTC:");
	//api
	return 0;
}


int main_menu_modules_3()
{
	printf("Текущий IP - адрес:");
	//api
	return 0;
}


int main_menu_modules_4()
{
	printf("Что бы вы хотели настроить?\n");
	printf("Изменить логин - 1\n");
	printf("Изменить пароль - 2\n");
	printf("Изменить аватар - 3\n");
	printf("Удалить аккаунт - 4\n");
	printf("Назад - 0\n");
	printf("Введите 1, 2, 3, 4 или 0: ");
	int user_choice4; cin >> user_choice4;
	string password_confirmation;
	switch(user_choice4)
	{
		case 1:
			printf("Для продолжения введите ваш пароль: ");
			cin >> password_confirmation;
			//
			printf("Логин успешно изменен!");
			break;
		case 2:
			printf("Для продолжения введите ваш пароль: ");
			cin >> password_confirmation;
			//
			printf("Пароль успешно изменен!");
			break;
		case 3:
			printf("Вставьте ссылку на ваш новый аватар");
			break;
		case 4:
			printf("Для продолжения введите ваш пароль: ");
			cin >> password_confirmation;
			//
			printf("Ваш аккаунт удален. До свидания!");
      		exit(1);
      		break;
	}
	return 0;
}


int main_menu_modules_5()
{ 
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
      printf("Вы можете просто связаться с разработчиком, если не верите в безопасность нашего чата.\n");
      break;
	case 3:
      printf("Специально для урегулирования вражды между компилируемыми и интерпретируемыми языками программирования программа для нашего чата написана на c ++ и python.\n");
      break;
	case 0:
      printf("НАЗАД\n");
      break;
	}
	return 0;
}


int main_menu_modules_6()	// Ready
{
	//std::cout << "До свидания, " << User.chel.user_login << "!";
	exit(1);
}


int main_menu_modules_0()
{
	printf("В настоящий момент я хикканю и у меня нет желания говорить.\n");
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
  	printf("Введите 1, 2, 3, 4, 5, 6 или 0: ");
  	int user_choice; cin >> user_choice;
  	switch (user_choice)
  	{
  		case 1:
  			main_menu_modules_1();
  			break;
  		case 2:
  			main_menu_modules_2();
  			break;
  		case 3:
  			main_menu_modules_3();
  			break;
  		case 4:
  			main_menu_modules_4();
  			break;
  		case 5:
  			main_menu_modules_5();
  			break;
  		case 6:
  			main_menu_modules_6();
  			break;
  		case 0:
  			main_menu_modules_0();
  			break;
  	}
  	main_menu();
  	return 0;
}


int new_user_registration()
{
	printf("Самое время зарегистрироваться. Введите свой новый логин: ");
	string new_user_login; getline(cin, new_user_login);
	cout << "Ваш новый логин: " << new_user_login << endl;
	printf("Самое время придумать пароль. Он должен содержать более 8ми символов: ");
	string new_user_password; getline(cin, new_user_password);
	printf("Введите свой новый пароль еще раз: ");
	string new_user_password_confirmation; getline(cin, new_user_password_confirmation);
	while (new_user_password != new_user_password_confirmation)
  	{
    	printf("Введенные пароли не сходятся. Попробуйте еще раз.\n");
    	cout << "Введите пароль: "; cin >> new_user_password_confirmation;
  	}
  	return 0; 
}


char get_old_login()
{
	printf("Введите свой логин: ");
	char login;
	cin >> login;
	return login;
}


char get_old_password()
{
	printf("Введите свой пароль: ");
	char password;
	cin >> password;
	return password;
}


int user_authentication()
{
	printf("Введите свой логин: ");
	string old_user_login; getline(cin, old_user_login);
	cout << "Ваш логин: " << old_user_login << endl;
	printf("Введите свой пароль: ");
	string old_user_password; getline(cin, old_user_password);
	return 0;
}

int get_user_answer()
{
	printf("Привет!\n");
	printf("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ");
	int user_answer; cin >> user_answer; cin.ignore(32767, '\n');
	return user_answer;
}

#endif
