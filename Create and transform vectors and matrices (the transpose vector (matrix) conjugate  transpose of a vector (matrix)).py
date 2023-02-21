import numpy as np

#Creating a Vector
vector = np.matrix([9, 8, 7])
print("Vector is:\n", vector )

vector_transpose = vector.T
print("\nTranspose of The Given Vector is:\n", vector_transpose)

# Creating a Matrix
mat1 = np.matrix([[6, 7+2j, 9], [5, 7, 1-4j], [2+5j, 0, 4-3j]])
print("\nMatrix is:\n",mat1)


matrix_transpose = np.transpose(mat1)
print("\nTranspose of The Given  Matrix is:\n", matrix_transpose)

# Conjugate Transpose of The Matrix

matrix_conjugate_transpose = np.conj(mat1.T)
print("\nConjugate Transpose of The Given matrix is:\n", matrix_conjugate_transpose)
