import numpy as np

def transpose_matrix(matrix):
    return np.transpose(matrix)

a = np.array([
    [7, 4, 7, 6, 6],
    [7, 5, 2, 5, 3],
    [9, 1, 3, 9, 4],
    [2, 3, 7, 3, 0],
    [8, 6, 8, 3, 9]
])
print(transpose_matrix(a))