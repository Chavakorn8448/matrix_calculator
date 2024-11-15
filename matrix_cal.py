import numpy as np
from input_matrix import get_one_metrix, get_two_metrix, print_metrix
from add_subtract_matrix_calc import add_matrices, subtract_matrices
from multiply import multiply_matrix
from transpose_matrix_calc import transpose_matrix
from determinant import determinant

def main():
    print("Choose the operation:")
    print("   1 - Addition")
    print("   2 - Subtraction")
    print("   3 - Multiplication")
    print("   4 - Finding determinants")
    print("   5 - Transpose")
    print("   6 - Inverse")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        matrix1, matrix2 = get_two_metrix()
        result = add_matrices(matrix1, matrix2)
        if result is not None:
            print("Sum:")
            print_metrix(result)
        pass

    elif choice == '2':
        matrix1, matrix2 = get_two_metrix()
        result = subtract_matrices(matrix1, matrix2)
        if result is not None:
            print("Differences:")
            print_metrix(result)
        pass

    elif choice == '3':
        matrix1, matrix2 = get_two_metrix()
        result = multiply_matrix(matrix1, matrix2)
        print(result)
        # print("Product:")
        # print_metrix(result)
        pass

    elif choice == '4':
        matrix1 = get_one_metrix()
        result = determinant(matrix1)
        print(f"Determinant: {result}")
        pass

    elif choice == '5':
        matrix = get_one_metrix()
        result = transpose_matrix(matrix)
        print("Transponsed Matrix:")
        print_metrix(result)
        pass

    elif choice == '6':
        pass
    else:
        print("Invalid choice")
    pass

if __name__ == "__main__":
    main()