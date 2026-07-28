# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================


def read_matrix(rows, columns):
    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i + 1}: ").split()
        row = []
        for j in range(columns):
            row.append(int(row_values[j]))
        matrix.append(row)
    return matrix


def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:>5}", end="")
        print()


def transpose_matrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    transpose = []
    for col in range(columns):
        new_row = []
        for row in range(rows):
            new_row.append(matrix[row][col])
        transpose.append(new_row)
    return transpose


def add_matrices(matrix_a, matrix_b):
    result = []
    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_a[i])):
            row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        return None

    result = []
    for i in range(rows_a):
        row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            row.append(total)
        result.append(row)
    return result


def main():
    print("Matrix Operations")
    print("1. Transpose")
    print("2. Add two matrices")
    print("3. Multiply two matrices")
    choice = int(input("Choose an option (1-3): "))

    if choice == 1:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
        matrix = read_matrix(rows, columns)
        print("\nOriginal Matrix:")
        display_matrix(matrix)
        print("\nTransposed Matrix:")
        display_matrix(transpose_matrix(matrix))
    elif choice == 2:
        rows = int(input("Enter number of rows: "))
        columns = int(input("Enter number of columns: "))
        print("Enter first matrix:")
        matrix_a = read_matrix(rows, columns)
        print("Enter second matrix:")
        matrix_b = read_matrix(rows, columns)
        print("\nResult:")
        display_matrix(add_matrices(matrix_a, matrix_b))
    elif choice == 3:
        rows_a = int(input("Enter number of rows for matrix A: "))
        cols_a = int(input("Enter number of columns for matrix A: "))
        rows_b = int(input("Enter number of rows for matrix B: "))
        cols_b = int(input("Enter number of columns for matrix B: "))
        print("Enter matrix A:")
        matrix_a = read_matrix(rows_a, cols_a)
        print("Enter matrix B:")
        matrix_b = read_matrix(rows_b, cols_b)
        result = multiply_matrices(matrix_a, matrix_b)
        if result is None:
            print("Error: The number of columns in A must equal the number of rows in B.")
        else:
            print("\nResult:")
            display_matrix(result)
    else:
        print("Invalid option.")


if __name__ == "__main__":
    main()

