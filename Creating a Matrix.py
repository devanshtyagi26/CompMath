import numpy as np

r1 = input("Row 1 ")
r2 = input("Row 2 ")
r3 = input("Row 3 ")

data = r1 + " ; " + r2 + ' ; ' + r3
print("\n Data: ",data) 
m = np.matrix(data)
print("\n",m)
print(" \nThanks for using this program... \nMade by Devansh Tyagi")