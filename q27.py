# _*_ coding: utf-8 _*_

"""题目：利用递归函数调用方式，将所输入的5个字符，以相反顺序打印出来。"""

def reverse(s):
    def f(s, s1):
        if not s:
            return s1
        s1 += s[-1]
        s = s[:-1]
        return f(s, s1)
    return f(s, '')


print(reverse('abcdefgh'))