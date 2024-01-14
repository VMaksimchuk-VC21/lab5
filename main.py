import random
import os


def input_matrix():
    return


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
            pass
        elif point == "2":
            pass

        elif point == "3":
            if 'result' in locals():
                answer = []
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
