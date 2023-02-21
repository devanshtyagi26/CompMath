import numpy as np
import sympy as sp

# Define the matrix
A = np.array([[3, 7, 9,],[5, 2, 1,],[-2, -9, 8]])

# Convert the matrix to a SymPy matrix
A_sym = sp.Matrix(A)

# Convert the matrix to its row echelon form
rref = A_sym.rref()[0]

# Convert the row echelon form back to a NumPy array
echelon = np.array(rref.tolist(), dtype=float)

#Rank of matrix
rank = np.linalg.matrix_rank(A)

# Print the echelon form and rank of the matrix
print("Echelon form:\n", echelon)
print("Rank:", rank)