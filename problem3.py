def sum_diagonals(matrix):
    primary_diagonal_sum = 0
    anti_diagonal_sum = 0
    if len(matrix)%2 == 0:
        for i in range(len(matrix)):
            primary_diagonal_sum += matrix[i][i]
        for i in range(len(matrix)):
            anti_diagonal_sum += matrix[i][-1-i]
        final_sum = primary_diagonal_sum + anti_diagonal_sum
        return final_sum
    else:
        for i in range(len(matrix)):
            primary_diagonal_sum += matrix[i][i]
        for i in range(len(matrix)):
            anti_diagonal_sum += matrix[i][-1-i]
        j = len(matrix)//2
        final_sum = primary_diagonal_sum + anti_diagonal_sum - matrix[j][j]
        return final_sum
    
matrix_4x4 = [
	[ 1,  2,  3,  4],
	[ 5,  6,  7,  8],
	[ 9, 10, 11, 12],
	[13, 14, 15, 16]
]
sum_of_matrix = sum_diagonals(matrix_4x4)
print(sum_of_matrix)

matrix_3x3 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]
sum_of_matrix = sum_diagonals(matrix_3x3)
print(sum_of_matrix)