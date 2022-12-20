import numpy as np
import math

n = int(input("enter the size of the matrix"))
A = np.zeros([n, n])

print("enter the coefficients")
for i in range(0, n):
    for j in range (0, n):
        A[i][j]=float(input())

v=np.ones(n)

for i in range(0, 100):
    v_new=np.dot(A, v)

    norm = v_new.max()
    #new vector
    v=v_new/norm
    lambda1 = np.max(v)

print(f'lambda = {lambda1}')