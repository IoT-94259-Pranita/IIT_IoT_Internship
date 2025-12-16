def matrix_operations(mat_list, mat_tuple):
    rows = len(mat_list)
    cols = len(mat_list[0])

    addition = []
    subtraction = []

    for i in range(rows):
        add_row = []
        sub_row = []
        for j in range(cols):
            add_row.append(mat_list[i][j] + mat_tuple[i][j])
            sub_row.append(mat_list[i][j] - mat_tuple[i][j])
        addition.append(add_row)
        subtraction.append(sub_row)

    return addition, subtraction

matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

add_result, sub_result = matrix_operations(matrix_list, matrix_tuple)

print("Addition of matrices:")
for row in add_result:
    print(row)

print("\nSubtraction of matrices:")
for row in sub_result:
    print(row)