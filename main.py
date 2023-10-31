import numpy as np

# Функція для перевірки циклів довжини 3 у матриці
def find_cycles(matrix):
    cycles = 0
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for k in range(len(matrix)):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                    cycles += 1
    return cycles

# Функція для обчислення коефіцієнта сумісності думок експертів
def calculate_competence(matrix):
    m = len(matrix)
    d = find_cycles(matrix)
    if m % 2 != 0:
        v = 1 - 24 * d / (m ** 3) - m
    else:
        v = 1 - 24 * d / (m ** 3) - 4 * m
    return v

# Приклад вхідних даних (матриці Ai)
expert_matrices = [
    np.array([[0, 1, 0, 1], [0, 0, 1, 0], [1, 0, 0, 1], [0, 0, 0, 0]]),
    np.array([[0, 0, 1, 0], [1, 0, 0, 1], [0, 1, 0, 0], [0, 0, 0, 0]]),
    # Додайте інші матриці експертів тут
]

# Розрахунок коефіцієнта сумісності думок для кожного експерта
for i, matrix in enumerate(expert_matrices):
    competence = calculate_competence(matrix)
    print(f"Коефіцієнт сумісності думок експерта {i+1}: {competence}")
