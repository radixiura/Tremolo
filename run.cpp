#include <iostream>
#include <cstring>
struct user
{
  const int ID;
  char name[20];
  char password[20];
};
int main()
{
using namespace std;
cout << "Hello.\n";
cout << "I am happy because you are using our chat - messenger." << endl;
cout << "What is your name?" << endl;
string new_user_name;
cin >> new_user_name;
cout << "Glad to see you, " << new_user_name << endl;
cout << "Now it is time to set your password\n";
//Блок создания нового пользователя
string new_user_password;
cin >> new_user_password;
return 0;
}

