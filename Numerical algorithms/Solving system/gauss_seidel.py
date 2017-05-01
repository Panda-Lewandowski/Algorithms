from math import sqrt


def gauss_seidel(A, b, eps):
    n = len(A)  # размерность матрицы
    x = [1 for i in range(n)]  # инициализация вектора(приближение)

    converge = False  # сходимость
    while not converge:
        x_new = x.copy()   # предыдущее приближение
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]

        converge = sqrt(sum((x_new[i] - x[i]) ** 2 for i in range(n))) <= eps
        x = x_new
    return x
