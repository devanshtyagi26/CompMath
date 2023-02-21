import numpy as np

#Creating a Matrix
matrix= np.array([6, 4, 9, 13, 22, 69], dtype=float)

#Finding Divergence of a Matrix

def divergence(x):
    return np.ufunc.reduce(np.add,np.gradient(x))

print("Input  :\n ", matrix)
print("Divergence :\n ",divergence(matrix))