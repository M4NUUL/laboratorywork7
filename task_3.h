#include <vector>
#include <algorithm>
using namespace std;

// Рекурсивная функция для размещения систем на компьютерах
bool canInstallRecursive(vector<int>& mem, const vector<int>& s, int idx) {
    if (idx == s.size()) return true; // все системы размещены
    for (int i = 0; i < mem.size(); ++i) {
        if (mem[i] >= s[idx]) {
            mem[i] -= s[idx];
            if (canInstallRecursive(mem, s, idx + 1)) return true;
            mem[i] += s[idx]; // backtrack
        }
    }
    return false;
}

// проверка можно ли инсталлировать все системы на компах
inline bool canInstallSystems(int m, const vector<int>& mem, int n, const vector<int>& s) {
    vector<int> memCopy = mem;
    vector<int> sCopy = s;
    sort(sCopy.rbegin(), sCopy.rend()); // сначала большие системы
    return canInstallRecursive(memCopy, sCopy, 0);
}
