import numpy as np

def matrix():
  data = ""
  size = int(input("Enter the size of matrix: "))
  print("\nDistinguish the elements by adding'space' in between.\n")
  for i in range(size):
    row = input("Enter row {}: ".format(i+1))       # Taking input from user
    data +=row        #Concatinating the elements
    if i != (size-1):
      data += " ; "
  print()
  try:
    global mat
    mat = np.matrix(data)       # WARNING if row size is not same 
    print("Original MATRIX:")
    print(mat)
    print()
  except ValueError:
    print("Rows should be of same size!! \n")


print("Transpose of the Vector")
print("\nDistinguish the elements by adding'space' in between.\n")
vec = input("Enter the Vector: ")
print("\nOriginal VECTOR")
vector = np.array(vec)
print(vector)
print("\nTranspose of the VECTOR")
print(vector.transpose())
print()
print("Transpose of a Matrix \n")
matrix()
print("Transpose of that MATRIX:")
print(mat.transpose())