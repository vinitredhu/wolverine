# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 15:57:38 2021

@author: DELL
"""
import numpy as np
import math

    
def cos_amplitude_method(mat):
    for i in range(c):
        for j in range(c):
            n = 0
            p = 0
            q = 0
            for k in range(r):
                n += mat[k][i]*mat[k][j]
                p += mat[k][i]**2
                q += mat[k][j]**2
            R[i][j]= n/math.sqrt(p*q)
    return R


r = int(input("Enter the number of classifications:"))
c = int(input("Enter the number of objects:"))

print("Enter the entries in a single line (separated by space): ")
entries = list(map(float, input().split()))

mat = np.array(entries).reshape(r, c)
print(mat)
R = np.zeros((c,c))
R = cos_amplitude_method(mat)
print("the tolerance relation is : \n",R)