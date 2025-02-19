import numpy as np
import scipy as sc


def matrix_multiplication(matrix_a, matrix_b):
    """
    Задание 1. Функция для перемножения матриц с помощью списков и циклов.
    Вернуть нужно матрицу в формате списка.
    """
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        raise ValueError("Число столбцов первйо матрицы не равно числу строк второй матрицы")

    result = [[0 for _ in range(cols_b)] for _ in range(rows_a)]

    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                result[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return result

    pass


def functions(a_1, a_2):
    """
    Задание 2. На вход поступает две строки, содержащие коэффициенты двух функций.
    Необходимо найти точки экстремума функции и определить, есть ли у функций общие решения.
    Вернуть нужно координаты найденных решения списком, если они есть. None, если их бесконечно много.
    """
    a11, a12, a13 = map(float, a_1.split())
    a21, a22, a23 = map(float, a_2.split())

    x1_extremum = None if a11 == 0 else -a12 / (2 * a11)
    x2_extremum = None if a21 == 0 else -a22 / (2 * a21)

    a = a11 - a21
    b = a12 - a22
    c = a13 - a23

    if a == 0 and b == 0 and c == 0:
        return None
    elif a == 0:
        if b != 0:
            x_solution = -c / b
            y_solution = a11 * x_solution**2 + a12 * x_solution + a13
            return [(x_solution, y_solution)]
        else:
            return []

    d = b**2 - 4 * a * c

    if d < 0:
        return []
    elif d == 0:
        x_solution = -b / (2 * a)
        y_solution = a11 * x_solution**2 + a12 * x_solution + a13
        return [(x_solution, y_solution)]
    else:
        x1_solution = (-b + d**0.5) / (2 * a)
        x2_solution = (-b - d**0.5) / (2 * a)
        y1_solution = a11 * x1_solution**2 + a12 * x1_solution + a13
        y2_solution = a11 * x2_solution**2 + a12 * x2_solution + a13
        return [(x1_solution, y1_solution), (x2_solution, y2_solution)]
    pass


def skew(x):
    """
    Задание 3. Функция для расчета коэффициента асимметрии.
    Необходимо вернуть значение коэффициента асимметрии, округленное до 2 знаков после запятой.
    """
    x = np.array(x)
    mean_x = np.mean(x)
    std_x = np.std(x)
    skewness = np.sum((x - mean_x) ** 3) / (len(x) * std_x ** 3)
    
    return round(skewness, 2)
    pass


def kurtosis(x):
    """
    Задание 3. Функция для расчета коэффициента эксцесса.
    Необходимо вернуть значение коэффициента эксцесса, округленное до 2 знаков после запятой.
    """
    x = np.array(x)
    mean_x = np.mean(x)
    std_x = np.std(x)
    
    n = len(x)
    kurt = np.sum((x - mean_x) ** 4) / (n * std_x ** 4) - 3
    
    return round(kurt, 2)
    pass
