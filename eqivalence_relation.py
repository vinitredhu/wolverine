# -*- coding: utf-8 -*-
"""
Created on Sun Apr 11 19:19:10 2021

@author: DELL
"""

a = int(input("enter the no of rows or colums in matrix"))
mat = [[float(input("enter element for {} row and {} column:".format(y+1,x+1)))for x in range (a)] for y in range(a)]
count = 0
for i in range(a):
    for j in range(a):
        lam0 = mat[i][j] 
        for k in range(a):
            lam1 = mat[j][k]
            lam2 = mat[i][k]
            if lam2 < min(lam0,lam1):
                print("not a equivalance relation")
                count += 1
if count == 0:
    print("equivalence relation")
wait = input("the end")
            