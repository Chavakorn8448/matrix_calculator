import numpy as np
from input_matrix import get_one_metrix, get_two_metrix, print_metrix
from add_subtract_matrix_calc import add_matrices, subtract_matrices
from multiply import multiply_matrix
from transpose_matrix_calc import transpose_matrix
from determinant import determinant
from multiply import multiply_matrix
from inverse import matrix_inverse

def main():
    while True:
        print("\nChoose the operation:")
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
                print("\nSum:")
                print_metrix(result)
        elif choice == '2':
            matrix1, matrix2 = get_two_metrix()
            result = subtract_matrices(matrix1, matrix2)
            if result is not None:
                print("\nDifferences:")
                print_metrix(result)
        elif choice == '3':
            matrix1, matrix2 = get_two_metrix()
            if len(matrix1[0]) == len(matrix2):
                result = multiply_matrix(matrix1, matrix2)
                if result is not None:
                    print("\nMultiplication:")
                    print_metrix(result)
            else:
                print("\nNumber of columns in the first matrix\nmust be equal to the number of rows in the second matrix")
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
                print("\nTranspose:")
                print_metrix(result)
            pass
        elif choice == '6':
            matrix1 = get_one_metrix()
            result = matrix_inverse(matrix1)
            if result is not None:
                print("\nInverse:")
                print_metrix(result)
            pass
        elif choice == '7':
            print("\nByeBye")
            return
        else:
            print("\nInvalid choice")
            pass

if __name__ == "__main__":
    main()
    