import numpy as np
from input_matrix import get_one_metrix, get_two_metrix, print_metrix
from add_subtract_matrix_calc import add_matrices, subtract_matrices
from transpose_matrix_calc import transpose_matrix
from determinant import determinant
from multiply import multiply_matrix

def main():
    print("Choose the operation:")
    print("   1 - Addition")
    print("   2 - Subtraction")
    print("   3 - Multiplication")
    print("   4 - Finding determinants")
    print("   5 - Transpose")
    print("   6 - Inverse")
    print("   7 - Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        matrix1, matrix2 = get_two_metrix()
        result = add_matrices(matrix1, matrix2)
        if result is not None:
            print("Sum:")
            print_metrix(result)
    elif choice == '2':
        matrix1, matrix2 = get_two_metrix()
        result = subtract_matrices(matrix1, matrix2)
        if result is not None:
            print("Differences:")
            print_metrix(result)
    elif choice == '3':
        matrix1, matrix2 = get_two_metrix()
        if len(matrix1[0]) == len(matrix2):
            result = multiply_matrix(matrix1, matrix2)
            if result is not None:
                print("Multiplication:")
                print_metrix(result)
        else:
            print("number of columns in the first matrix must be equal to the number of rows in the second matrix")

    elif choice == '4':
        matrix1 = get_one_metrix()
        if matrix1.shape[0] == matrix1.shape[1]:
            result = determinant(matrix1)
            if result is not None:
                print("Determinant:")
                print(result)
        else:
            print("Input must be a square matrix. ")
            
    elif choice == '5':
        matrix1 = get_one_metrix()
        result = transpose_matrix(matrix1)
        if result is not None:
            print("Transpose:")
            print_metrix(result)
    elif choice == '6':
        pass
    elif choice == '7':
        return
    else:
        print("Invalid choice")
        pass

if __name__ == "__main__":
    main()