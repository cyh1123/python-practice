# -*- coding: UTF-8 -*-

"""两个 3 行 3 列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵：

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]"""
import numpy

X = [[12,7,3],
    [4 ,5,6],
    [7 ,8,9]]

Y = [[5,8,1],
    [6,7,3],
    [4,5,9]]

def matrixadd(x, y):
    L1 = []
    for i in range(len(x)):
        L2 = []
        for j in range(len(x)):
            L2 += [x[i][j] + y[i][j]]
        L1 += [L2]
    return L1

def npadd(x, y):
    m = numpy.array(x)
    n = numpy.array(y)
    return m + n


print(npadd(X, Y))
