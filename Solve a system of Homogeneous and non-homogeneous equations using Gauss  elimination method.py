import numpy as np

# Get the input from the user
n = int(input("Enter the number of equations: "))
A = np.zeros((n, n))
b = np.zeros(n)

print("Enter the coefficients of the matrix A row-wise (using space in between):")
for i in range(n):
    A[i] = np.array(input().split(), float)

print("Enter the values of b (using space in between):")
b = np.array(input().split(), float)

# Solve the system of linear equations using linalg.solve
x = np.linalg.solve(A, b)

# Print the solution
print("Solution to the system of linear equations:")
print(x)
