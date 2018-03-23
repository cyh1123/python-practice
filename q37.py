# -*- coding: UTF-8 -*-

"""题目：对10个数进行排序。"""

def mysort(n):
    L = []
    for i in range(1, n+1):
        num = int(input('input %sth number: ' % i))
        L.append(num)
    L.sort()
    return L




def mysort2(n):
    L = []
    for i in range(1, n+1):
        num = int(input('input %sth number: ' % i))
        if len(L) == 0:
            L.append(num)
        elif num >= L[-1]:
            L.append(num)
        elif num <= L[0]:
            L.insert(0, num)
        else:
            for j in range(len(L)):
                if L[j] < num <= L[j+1]:
                    L.insert(j+1, num)
                    break
    return L


print(mysort2(9))