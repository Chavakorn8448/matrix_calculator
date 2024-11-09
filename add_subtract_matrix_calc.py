import numpy as np

def add_matrices(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        print(f"Dimensions are different.\nMatrix 1: {matrix1.shape}\nMatrix 2: {matrix2.shape}\nCannot Add")
        return None
    return matrix1 + matrix2 

def subtract_matrices(matrix1, matrix2):
    if matrix1.shape != matrix2.shape:
        print(f"Dimensions are different.\nMatrix 1: {matrix1.shape}\nMatrix 2: {matrix2.shape}\nCannot Subtract")
        return None
    return matrix1 - matrix2  
