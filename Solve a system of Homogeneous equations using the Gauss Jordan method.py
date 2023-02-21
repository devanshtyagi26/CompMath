import numpy as np

# Get the input from the user
n = int(input("Enter the number of equations: "))
A = np.zeros((n, n))
B = np.zeros(n)

print("Enter the coefficients of the matrix A row-wise (using space in between):")
for i in range(n):
    A[i] = np.array(input().split(), float)

print("Enter the values of B (using space in between):")
B = np.array(input().split(), float)

# Solve the system of linear equations using linalg.solve
A_inv = np.linalg.inv(A)
x = np.dot(A_inv, B)

# Print the solution
print("Solution to the system of linear equations:")
print(x)