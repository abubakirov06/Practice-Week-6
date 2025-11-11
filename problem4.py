def transpose_matrix(matrix):
    new_inner_matrix = []
    new_matrix = []
    for i in range(len(matrix[0])):
        for j in range(len(matrix)):
            new_inner_matrix.append(matrix[j][i])
        new_matrix.append(new_inner_matrix)
        new_inner_matrix = []
    return new_matrix

print()
matrix_3x2 = [
	[1, 2],
	[3, 4],
	[5, 6]
]

new_matrix = transpose_matrix(matrix_3x2)
for element in new_matrix:
    print(element)

matrix_2x2 = [
	['a', 'b'],
	['c', 'd']
]
print()
new_matrix = transpose_matrix(matrix_2x2)
for element in new_matrix:
    print(element)


