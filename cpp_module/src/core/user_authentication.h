#ifndef USER_AUTHENTICATION_H
#define USER_AUTHENTICATION_H


using namespace std;


int user_authentication()
{
	printf("Введите свой логин: ");
	string user_login; getline(cin, user_login);
	cout << "Ваш логин: " << user_login << endl;
	printf("Введите свой пароль: ");
	string user_password; getline(cin, user_password);
	return 0;
}


#endif
