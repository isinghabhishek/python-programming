# Python program to print checkerboard pattern of nxn using numpy

import numpy as np

def printCheckBoard(n):
    print("CheckBoard Pattern:")

    x = np.zeros((n, n), dtype = int)

    x[1::2, ::2] = 1
    x[::2, 1::2] = 1

    for i in range(n):
        for j in range(n):
            print(x[i][j], end =" ")
        print()
    
n = int(input("Enter The No: "))
printCheckBoard(n)