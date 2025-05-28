def can_install_systems(m, mem, n, s):
    mem_copy = sorted(mem, reverse=True)
    s_copy = sorted(s, reverse=True)
    if n > m:
        return False
    for i in range(n):
        if s_copy[i] > mem_copy[i]:
            # не хватает памяти
            return False
    return True

if __name__ == "__main__":
    m = int(input("Введите количество компьютеров: "))
    mem = list(map(int, input("Введите объемы памяти компьютеров через пробел: ").split()))
    if len(mem) != m:
        print(f"Ошибка: введено {len(mem)} значений, а ожидалось {m}.")
        exit(1)
    n = int(input("Введите количество систем: "))
    s = list(map(int, input("Введите требования к памяти систем через пробел: ").split()))
    if len(s) != n:
        print(f"Ошибка: введено {len(s)} значений, а ожидалось {n}.")
        exit(1)
    if can_install_systems(m, mem, n, s):
        print("Можно установить все системы")
    else:
        print("Нельзя установить все системы")
