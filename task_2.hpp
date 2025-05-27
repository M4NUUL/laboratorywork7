#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;


// Рекурсивная версия поиска минимального количества повторений для получения суммы
int minRepeatsHelper(int sum, const vector<int> &arr, vector<int> &memo) {
   if (sum == 0) return 0;
   if (sum < 0) return -1;
   if (memo[sum] != -2) return memo[sum];
   int min_count = -1;
   for (int num : arr) {
      int res = minRepeatsHelper(sum - num, arr, memo);
      if (res != -1) {
         if (min_count == -1 || res + 1 < min_count)
            min_count = res + 1;
      }
   }
   memo[sum] = min_count;
   return min_count;
}

int minRepeats(int sum, const vector<int> &arr) {
   vector<int> memo(sum + 1, -2); // -2: not computed, -1: impossible, >=0: min count
   return minRepeatsHelper(sum, arr, memo);
}
