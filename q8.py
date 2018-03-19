# _*_ coding: utf-8 _*_

"""题目：输出 9*9 乘法口诀表。"""

def table(n):
    for row in range(1, n+1):
        L = []
        for col in range(1, row+1):
            f = '%2d * %d = %2d' % (col, row, row*col)
            L.append(f)
        print(' '.join(L))

table(9)
