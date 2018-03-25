# -*- coding: UTF-8 -*-

"""题目：将一个数组逆序输出。"""
# quote from q27.py


def reverse(s):
    def f(s, s1):
        if not s:
            return s1
        s1 += [s[-1]]
        return f(s[:-1], s1)
    return f(s, [])

def reverse2(s):
    for i in range(int(len(s)/2)):
        s[i], s[-i-1] = s[-i-1], s[i]
    return s

print(reverse2([1,1,2,3,5,8,13,21,34]))
