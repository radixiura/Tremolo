#ifndef FUNCTIONS_H
#define FUNCTIONS_H
                                                                                                                                       

using namespace std;

# Функция приветствия
int greetings()
{
	printf("Привет!\n");
	printf("Вы уже имеете аккаунт? Введите 1 если да, 0 если нет: ");
	int user_answer; cin >> user_answer; cin.ignore(32767, '\n');
	return user_answer;
}


#endif
