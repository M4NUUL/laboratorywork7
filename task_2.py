def min_repeats_helper(s, arr, memo):
    if s == 0:
        return 0
    if s < 0:
        return -1
    if memo[s] != -2:
        return memo[s]
    min_count = -1
    for num in arr:
        res = min_repeats_helper(s - num, arr, memo)
        if res != -1:
            if min_count == -1 or res + 1 < min_count:
                min_count = res + 1
    memo[s] = min_count
    return min_count

def min_repeats(s, arr):
    memo = [-2] * (s + 1)  # -2: not computed, -1: impossible, >=0: min count
    return min_repeats_helper(s, arr, memo)

if __name__ == "__main__":
    arr = list(map(int, input("Введите числа через пробел: ").split()))
    s = int(input("Введите сумму: "))
    result = min_repeats(s, arr)
    if result == -1:
        print("Невозможно получить сумму")
    else:
        print("Минимальное количество повторений:", result)
