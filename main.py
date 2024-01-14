import random
import os


def input_matrix():
    input_matrix = input("Выберите тип ввода данных:\n"
                         "1. вручную\n"
                         "2. сгенерировать случайным образом\nВведите тип ввода данных: ")
    if input_matrix == '1':
        n = input("Введите количество строк: ")
        while not n.isdigit():
            os.system("cls")
            print("Введите целочисленное значение для количества строк")
            n = input("Введите количество строк: ")

        m = input("Введите количество столбцов: ")
        while not m.isdigit():
            os.system("cls")
            print("Введите целочисленное значение для количества столбцов")
            m = input("Введите количество столбцов: ")

        matrix = []
        print("Введите элементы матрицы:")
        for i in range(int(n)):
            row = []
            for j in range(int(m)):
                element = input(f"Введите элемент [{i}, {j}]: ")
                while not element.isdigit():
                    os.system("cls")
                    print("Введите целочисленное значение")
                    element = input(f"Введите элемент [{i}, {j}]: ")
                row.append(int(element))
            matrix.append(row)

    elif input_matrix == '2':
        n = input("Введите количество строк: ")
        while not n.isdigit():
            os.system("cls")
            print("Введите целочисленное значение для количества строк")
            n = input("Введите количество строк: ")

        m = input("Введите количество столбцов: ")
        while not m.isdigit():
            os.system("cls")
            print("Введите целочисленное значение для количества столбцов")
            m = input("Введите количество столбцов: ")

        matrix = []
        for i in range(int(n)):
            row = []
            for j in range(int(m)):
                element = random.randint(0, 100)
                row.append(element)
            matrix.append(row)
    else:
        os.system("cls")
        print("Неверный тип ввода данных")
        matrix = None

    return matrix


def dot(matrix):
    answer = []
    for i, row in enumerate(matrix):
        min_dot = min(row)
        for j, element in enumerate(row):
            if element == min_dot:
                dot = [matrix[k][j] for k in range(len(matrix))]
                max_dot = max(dot)
                if element == max_dot:
                    answer.append(element)

    return answer


def main():
    while True:
        os.system("cls")
        print("\nМеню:")
        print("1. Ввод исходных данных")
        print("2. Решение задания")
        print("3. Результат работы алгоритма")
        print("4. Завершение работы программы")

        point = input("Введите пункт меню: ")

        if point == "1":
            matrix = input_matrix()
        elif point == "2":
            if 'matrix' in locals():
                result = dot(matrix)
                print("Исходная матрица:", matrix)
                print("Задание решено")
            else:
                print("Массив не введен")
        elif point == "3":
            if 'result' in locals():
                answer = result
                print("Результат:")
                print("Массив седловых точек:", answer)
            else:
                print("Входные данные не сгенерированы")
        elif point == "4":
            print("Программа завершена")
            break
        else:
            os.system("cls")
            print("Выберите верный пункт меню")


if __name__ == '__main__':
    main()
