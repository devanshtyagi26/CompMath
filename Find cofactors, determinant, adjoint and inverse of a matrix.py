import numpy as np

def cofactor(matrix):
    n = matrix.shape[0]
    result = np.zeros((n, n))

    for i in range(n):
        for j in range(n):
            sub_matrix = matrix[np.array(list(range(i))+list(range(i+1,n)))[:,np.newaxis], 
                                np.array(list(range(j))+list(range(j+1,n)))]
            result[i,j] = (-1)**(i+j) * np.linalg.det(sub_matrix)

    return result

# Example matrix
A = np.array([[2, 0, -1], [5, 1, 0], [0, 1, 3]])

# Cofactor matrix
C = cofactor(A)

# Determinant
det = np.linalg.det(A)

# Adjoint matrix (transpose of cofactor matrix)
adj = C.T


print("Original Matrix:\n", A)
print("Cofactor matrix:\n", C)
print("Determinant:", det)
print("Adjoint matrix:\n", adj)
# Inverse matrix (adjoint matrix divided by determinant)
if det == 0:
    print("Matrix is singular, inverse does not exist.")
else:
    A_inv = adj / det
    print("Inverse matrix:\n", A_inv)