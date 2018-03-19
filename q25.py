# _*_ coding: utf-8 _*_

"""题目：求1+2!+3!+...+20!的和。"""



def cal(n):
    def s(a, b, c, n):
        if c > n:
          return a
        a += b
        c += 1
        b *= c
        return s(a, b, c, n)
    return s(0, 1, 1, n)



print(cal(20))