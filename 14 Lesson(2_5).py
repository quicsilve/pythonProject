def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append (value)
    print(matrix)
    return matrix

n = int(input("Строки: "))
m = int(input("Столбцы: "))
value = input(f"Значение: ")
matrix1 = get_matrix(n, m, value)

if n <= 0:
    print("Матрица пуста, задано неверное количество строк:")
elif m <=0:
    print("Матрица пуста, задано неверное количество столбцов:")