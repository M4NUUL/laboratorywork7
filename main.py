from task_1 import drawing
from task_2 import min_repeats
from task_3 import can_install_systems

def main():
    print("Выберите номер задачи (1-3): ", end="")
    try:
        choice = int(input())
    except ValueError:
        print("Неверный выбор. Пожалуйста, выберите задачу 1, 2 или 3.")
        return

    if choice == 1:
        try:
            depth = int(input("Введите глубину рекурсии для треугольника Серпинского: "))
            if depth < 0:
                print("Глубина должна быть от 0.")
                return
            drawing(depth)
        except ValueError:
            print("Ошибка ввода.")
    elif choice == 2:
        try:
            s = int(input("Введите сумму: "))
            n = int(input("Введите количество номиналов монет: "))
            print("Введите номиналы монет через пробел: ", end="")
            coins = list(map(int, input().split()))
            if len(coins) != n:
                print("Количество номиналов не совпадает с введённым числом.")
                return
            result = min_repeats(s, coins)
            if result == -1:
                print("Невозможно получить сумму этими монетами.")
            else:
                print("Минимальное количество монет:", result)
        except ValueError:
            print("Ошибка ввода.")
    elif choice == 3:
        try:
            m = int(input("Введите количество компьютеров: "))
            print("Введите свободную память на каждом компьютере через пробел: ", end="")
            mem = list(map(int, input().split()))
            n = int(input("Введите количество систем: "))
            print("Введите требования к памяти для каждой системы через пробел: ", end="")
            s = list(map(int, input().split()))
            if len(mem) != m or len(s) != n:
                print("Количество введённых значений не совпадает с указанным.")
                return
            if can_install_systems(m, mem, n, s):
                print("Можно инсталлировать все системы на компьютеры.")
            else:
                print("Невозможно инсталлировать все системы на компьютеры.")
        except ValueError:
            print("Ошибка ввода.")
    else:
        print("Неверный выбор. Пожалуйста, выберите задачу 1, 2 или 3.")

if __name__ == "__main__":
    main()
