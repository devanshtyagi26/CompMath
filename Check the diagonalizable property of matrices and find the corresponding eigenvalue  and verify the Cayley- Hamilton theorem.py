import numpy as np

# Define the matrix to be checked
A = np.array([[2, 1], [1, 2]])

# Compute the eigenvalues and eigenvectors of A
eigenvalues, eigenvectors = np.linalg.eig(A)

# Print the eigenvalues and eigenvectors
print("Eigenvalues:")
print(eigenvalues)
print("Eigenvectors:")
print(eigenvectors)

# Check if A is diagonalizable
if np.allclose(A, np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))):
    print("A is diagonalizable")
else:
    print("A is not diagonalizable")

# Verify the Cayley-Hamilton theorem
pA = np.polyval(np.array([1, -np.trace(A), np.linalg.det(A)]), A)
if np.allclose(pA, np.zeros_like(A)):
    print("Cayley-Hamilton theorem holds for A")
else:
    print("Cayley-Hamilton theorem does not hold for A")