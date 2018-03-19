# _*_ coding: utf-8 _*_

"""题目：利用递归方法求5!。"""

def fact(n):
    def f(n, s):
        if n == 1:
            return s
        s *= n
        return f(n-1, s)
    return f(n, 1)

print(fact(5))