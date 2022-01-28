#ifndef NEW_USER_REGISTRATION_H
#define NEW_USER_REGISTRATION_H


using namespace std;


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


#endif
