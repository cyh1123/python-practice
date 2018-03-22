# _*_ coding: utf-8 _*_

"""题目：按相反的顺序输出列表的值。"""

def reve(L):
    for i in range(1, len(L)+1):
        print(L[-i])


reve('abcdefg')

