#include <vector>
#include <algorithm>
using namespace std;

// проверка можно ли инсталлировать все системы на компах
inline bool canInstallSystems(int m, const vector<int>& mem, int n, const vector<int>& s) {
    vector<int> memCopy = mem;
    vector<int> sCopy = s;
    sort(memCopy.rbegin(), memCopy.rend());
    sort(sCopy.rbegin(), sCopy.rend());
    if (n > m) return false;
    for (int i = 0; i < n; ++i) {
        if (sCopy[i] > memCopy[i]) {
            // не хватает паммяти
            return false;
        }
    }
    return true;
}
