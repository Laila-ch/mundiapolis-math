#!/usr/bin/env python3
def matrix_shape(matrix) : 
    i=0
    list=[]
    for row in matrix : 
        i=i+1
        j=0
        for r in row : 
            j=j+1
    list.append(i)
    list.append(j)
    return list
mat1 = [[1, 2], [3, 4]]
print(matrix_shape(mat1))
mat2 = [[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15]],
        [[16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]]
print(matrix_shape(mat2))
