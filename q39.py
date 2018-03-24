# -*- coding: UTF-8 -*-

"""题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。"""
# quote from q37.py


def mysort(L):
    num = int(input('input a number: '))
    if len(L) == 0:
        L.append(num)
    elif num >= L[-1]:
        L.append(num)
    elif num <= L[0]:
        L.insert(0, num)
    else:
        for j in range(len(L)):
            if L[j] < num <= L[j + 1]:
                L.insert(j + 1, num)
                break

    return L


print(mysort([1,1,2,3,5,8]))
