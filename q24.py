# _*_ coding: utf-8 _*_

"""题目：有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13...求出这个数列的前20项之和。"""

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def s(n):
    t = 0
    for i in range(1, n+1):
        t += fib(i+2)/fib(i+1)
    return t

print(s(20))
        