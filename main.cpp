#include <iostream>
#include <vector>
#include "task_1.h"
#include "task_2.h"
#include "task_3.h"

using namespace std;

int main()
{
   int choice = 0;
   cout << "Выберите номер задачи (1-3): ";
   cin >> choice;

   switch (choice)
   {
   case 1:
   {
      int depth;
      cout << "Введите глубину рекурсии для треугольника Сперлинского: ";
      cin >> depth;
      if (depth < 0)
      {
         cout << "Глубина должна быть от 0." << endl;
         return 1;
      }
      drawing(depth);
      break;
   }
   case 2:
   {
      int sum;
      int n;
      cout << "Введите сумму: ";
      cin >> sum;
      cout << "Введите количество номиналов монет: ";
      cin >> n;
      vector<int> coins(n);
      cout << "Введите номиналы монет через пробел: ";
      for (int i = 0; i < n; ++i)
      {
         cin >> coins[i];
      }
      int result = minRepeats(sum, coins);
      if (result == -1)
      {
         cout << "Невозможно получить сумму этими монетами." << endl;
      }
      else
      {
         cout << "Минимальное количество монет: " << result << endl;
      }
      break;
   }
   case 3:
   {
      int m, n;
      cout << "Введите количество компьютеров: ";
      cin >> m;
      vector<int> mem(m);
      cout << "Введите свободную память на каждом компьютере через пробел: ";
      for (int i = 0; i < m; ++i) cin >> mem[i];
      cout << "Введите количество систем: ";
      cin >> n;
      vector<int> s(n);
      cout << "Введите требования к памяти для каждой системы через пробел: ";
      for (int i = 0; i < n; ++i) cin >> s[i];
      if (canInstallSystems(m, mem, n, s)) {
         cout << "Можно инсталлировать все системы на компьютеры." << endl;
      } else {
         cout << "Невозможно инсталлировать все системы на компьютеры." << endl;
      }
      break;
   }
   default:
      cout << "Неверный выбор. Пожалуйста, выберите задачу 1, 2 или 3." << endl;
   }

   return 0;
}