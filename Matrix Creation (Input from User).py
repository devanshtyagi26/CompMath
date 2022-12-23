import numpy as np
def matrix():
  data = ""
  for i in range(3):
    row = input("Enter row {}: ".format(i+1))       # Taking input from user
    data +=row        #Concatinating the elements
    if i != 2:
      data += " ; "
  print()
  try:
    mat = np.matrix(data)       # WARNING if row size is not same 
    print(mat)
    print()
  except ValueError:
    print("Rows should be of same size!! \n")

print("Creating MATRICES \n")
while True:       #Loop for continuously creating Matrices
  matrix()
  cond = input("Do you want to continue? (Y/N)  ")
  print()
  if cond not in "Yy":
    print(" \nThanks for using this program... \nMade by Devansh Tyagi")
    break
