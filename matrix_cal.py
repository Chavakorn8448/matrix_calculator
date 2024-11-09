import numpy as np
from input_matrix import get_one_metrix, get_two_metrix, print_metrix
from add_subtract_matrix_calc import add_matrices, subtract_matrices
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
    print("   7 - Exit")
    
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
        pass
    elif choice == '4':
        pass
    elif choice == '5':
        pass
    elif choice == '6':
        pass
    elif choice == '7':
        return
    else:
        print("Invalid choice")
        pass

if __name__ == "__main__":
    main()