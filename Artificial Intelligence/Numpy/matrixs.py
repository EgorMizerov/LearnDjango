import numpy as np

matrix = np.array([[5, 2, 8],
                   [4, 9, 1],
                   [0, 0, 0]])

matrix_rel = np.array([[1, 5, 2],
                       [0, 0, 3],
                       [1, 3, 8]])

# Matrix Subtract
matrix_sub = matrix - matrix_rel
# [ 4  -3   6]
# [ 4   9  -2]
# [-1  -3  -8]

# Matrix Addition
matrix_rev = matrix + matrix_sub
# [ 6 7 10 ]
# [ 4 9  4 ]
# [ 1 3  8 ]

# Matrix DotProduct
matrix_mul = np.dot(matrix,matrix_rev)
# [ 13 49 80 ]
# [  5 23 43 ]
# [  0  0  0 ]

# Matrix Non-Div
matrix_as_row = np.array([[1, 3, 6],
                          [4, 5, 7],
                          [1, 3, 7]])
# non_invertible_matrix = inv(matrix_as_row)
# LinAlgError: Singular Matrix
