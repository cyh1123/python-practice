# _*_ coding: utf-8 _*_

"""题目：给一个不多于5位的正整数，要求：一、求它是几位数，二、逆序打印出各位数字。"""

def manu(num):
    n = str(num)
    print('length of the number: %s' % len(n))
    def f(n):
        if len(n) == 0:
            return
        print(n[-1])
        return f(n[:-1])
    f(n)

manu(142857)