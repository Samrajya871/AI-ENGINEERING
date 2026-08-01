import numpy as np
matrix1 = np.array([[1,2],[3,4]])
matrix2 = np.array([[5,6],[7,8]])

def display_matrices(matrix1, matrix2):
    print("Matrix 1:")
    print(matrix1)

    print("Matrix 2:")
    print(matrix2)

def matrix_shape(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return True
    else:
        print("Matrices must have the same dimensions")
        return False

def add(matrix1, matrix2):
    if matrix_shape(matrix1, matrix2):
        print(matrix1 + matrix2)

def sub(matrix1, matrix2):
    if matrix_shape(matrix1, matrix2):
        print(matrix1-matrix2)

def mul(matrix1, matrix2):
    if matrix_shape(matrix1, matrix2):
        print(matrix1 * matrix2)

def matrix_mul(matrix1, matrix2):
    if matrix1.shape[1] == matrix2.shape[0]: #no of columns in 1st matrix must be equal to 2nd matrix rows
        print(np.matmul(matrix1,matrix2)) #also matrix1 @ matrix2

    else:
        print("Matrix multiplication is not possible.")
def transpose_A(matrix1):
    print(matrix1.T)

def transpose_B(matrix2):
    print(matrix2.T)

def scalar_A(matrix1):
    scalar = int(input("Enter scalar: "))
    print(matrix1 * scalar)

def scalar_B(matrix2):
    scalar = int(input("Enter scalar"))
    print(matrix2 * scalar)

def detreminant_A(matrix1): #determinant only works for square matrices
    if matrix1.shape[0] == matrix1.shape[1]:
        print(np.linalg.det(matrix1))
    else:
        print("Determinant can only be calculated for square matrices.")

def detreminant_B(matrix2): #determinant only works for square matrices
    if matrix2.shape[0] == matrix2.shape[1]:
        print(np.linalg.det(matrix2))
    else:
        print("Determinant can only be calculated for square matrices.")

while True:

    print("1. Display Matrices")
    print("2. Addition")
    print("3. Subtraction")
    print("4. Multiplication")
    print("5. Matrix Multiplication")
    print("6. Transpose of A")
    print("7. Transpose of B")
    print("8. Scalar multiplication of A")
    print("9. Scalar multipcation with B")
    print("10. Determinant of A")
    print("11. Determinant of B")
    print("12. Exit")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        display_matrices(matrix1, matrix2)

    elif choice == 2:
        add(matrix1, matrix2)

    elif choice == 3:
        sub(matrix1, matrix2)
    elif choice==4:
        mul(matrix1, matrix2)
    elif choice == 5:
        matrix_mul(matrix1, matrix2)

    elif choice == 6:
        transpose_A(matrix1)

    elif choice == 7:
        transpose_B(matrix2)

    elif choice == 8:
        scalar_A(matrix1)

    elif choice == 9:
        scalar_B(matrix2)

    elif choice == 10:
        detreminant_A(matrix1)

    elif choice == 11:
        detreminant_B(matrix2)

    elif choice == 12:
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")