from numpy.random import choice
import numpy as np
import math
n = int(input("ΕΙΣΑΓΕΤΕ ΤΙΣ ΔΙΑΣΤΑΣΕΙΣ:"))

a = [0]*n**2
b = [1]*math.ceil((n**2)/2)
def swap_elements(x, t):

    new_x = x[:]
    for idx, value in zip(choice(range(len(x)), size=len(t), replace=False), t):
        new_x[idx] = value
    return new_x

sum = 0
p=1
while p <= 100:
    swapped = swap_elements(a, b)
    w = np.array(swapped).reshape(n, n)
    c = 0
    #horizontal
    for i in range(0, n):
         for j in range(0, n-3):
            if w[i][j] == w[i][j+1] == w[i][j+2] == w[i][j+3] == 1:
                c += 1
    #vertical
    for i in range(0, n-3):
        for j in range(0, n):
            if w[i][j] == w[i+1][j] == w[i+2][j] == w[i+3][j] == 1:
                c += 1
    #diagonal \
    for i in range(0, n-3):
        for j in range(0, n-3):
            if w[i][j] == w[i+1][j+1] == w[i+2][j+2] == w[i+3][j+3] == 1:
                c += 1
    #diagonal /
    for i in range(0, n-3):
        for j in range(3, n):
            if w[i][j] == w[i+1][j-1] == w[i+2][j-2] == w[i+3][j-3] == 1:
                c += 1
    p += 1
    sum = sum+c
average = sum/100
print(average)

