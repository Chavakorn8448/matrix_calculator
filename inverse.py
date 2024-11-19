import numpy as np

def matrix_inverse(matrix):
    """
    Function to calculate the inverse of a given square matrix, with elements rounded to 3 significant figures.
    If the matrix is singular, prints an error message and returns None.

    Parameters:
    matrix (list or np.ndarray): A square matrix (2D list or numpy array).

    Returns:
    np.ndarray: Inverse of the matrix with elements rounded to 3 significant figures if it exists.
    None: If the matrix is singular or not square.
    """
    try:
        # Convert the input to a numpy array
        matrix = np.array(matrix, dtype=float)
        # Check if the matrix is square
        if matrix.shape[0] != matrix.shape[1]:
            print("Error: Matrix must be square to compute its inverse.")
            return None

        # Round the input matrix to 3 significant figures
        matrix = np.round(matrix, decimals=3)

        # Calculate the inverse
        inv_matrix = np.linalg.inv(matrix)

        # Round the inverse matrix to 3 significant figures
        inv_matrix = np.round(inv_matrix, decimals=3)

        return inv_matrix
    except np.linalg.LinAlgError:
        print("Error: Matrix is singular and cannot be inverted.")
        return None
