# _*_ coding: utf-8 _*_

"""题目：求一个3*3矩阵主对角线元素之和。"""
import numpy

matrix = numpy.random.randint(1, 100, (3, 3))

for i in range(matrix.shape[0]):
    print(matrix[i][i])





