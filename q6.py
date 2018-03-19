# _*_ coding: utf-8 _*_

"""题目：斐波那契数列。"""

def fib1(n):
    if n == 1 or n == 2:
        return 1
    return fib1(n - 1) + fib1(n - 2)
# 第n个斐波那契数


def fib2(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a
# 第n个斐波那契数


def fibseq(n):
    L = []
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
        L.append(a)
    return L


print(fibseq(11))
