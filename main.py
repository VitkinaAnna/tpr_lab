def build_preference_matrix(input_matrix):
    m = len(input_matrix)
    preference_matrices = []

    for i in range(m):
        preference_matrix = []
        for j in range(m):
            preference_row = []
            for k in range(m):
                if j == k:
                    preference_row.append(0)  # Діагональ заповнена нулями
                else:
                    if input_matrix[i][j] > input_matrix[i][k]:
                        preference_row.append(1)
                    else:
                        preference_row.append(0)
            preference_matrix.append(preference_row)
        preference_matrices.append(preference_matrix)

    return preference_matrices

def find_cycles(matrix):
    cycles = []
    m = len(matrix)

    for i in range(m):
        for j in range(m):
            for k in range(m):
                if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                    cycle = [i, j, k]
                    cycles.append(cycle)

    return cycles

def count_cycles(matrix):
    count = 0
    m = len(matrix)
    for i in range(m):
        for j in range(m):
            for k in range(m):
                if i != j and j != k and k != i:
                    if matrix[i][j] == 1 and matrix[j][k] == 1 and matrix[k][i] == 1:
                        count += 1
    return count

def compatibility_coefficient(matrix):
    m = len(matrix)
    d = count_cycles(matrix)
    if m % 2 == 1:
        v = 1 - 24 * d / m**3 - m
    else:
        v = 1 - 24 * d / m**3 - 4 * m
    return v

def compute_and_print_compatibility_coefficients(preference_matrices):
    for i, matrix in enumerate(preference_matrices):
        v = compatibility_coefficient(matrix)
        print(f"Оцінка компетентрості експерта {i + 1}: {v}")


def print_preference_matrices(preference_matrices):
    for i, matrix in enumerate(preference_matrices):
        print(f"Відношення переваги експерта {i + 1}:")
        for row in matrix:
            print(row)
        print()

def compute_sum_of_matrices(matrices):
    m = len(matrices)
    sum_matrix = [[0 for _ in range(m)] for _ in range(m)]

    for matrix in matrices:
        for i in range(m):
            for j in range(m):
                sum_matrix[i][j] += matrix[i][j]

    return sum_matrix

# Початкова матриця
input_matrix = [
    [0, 1, 0, 1],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0]
]

preference_matrices = build_preference_matrix(input_matrix)
print_preference_matrices(preference_matrices)
compute_and_print_compatibility_coefficients(preference_matrices)
sum_of_matrices = compute_sum_of_matrices(preference_matrices)

print("----------")

found_cycles = find_cycles(input_matrix)
print("Цикли довжини 3 у матриці:")
for cycle in found_cycles:
    print(cycle)

print("----------")

print("Сума матриць переваг:")
for row in sum_of_matrices:
    print(row)

print("----------")

found_cycles = find_cycles(sum_of_matrices)
print("Цикли довжини 3 у матриці:")
for cycle in found_cycles:
    print(cycle)

print("----------")

v = compatibility_coefficient(sum_of_matrices)
print("Коефіцієнт сумісності думок експертів:", v)