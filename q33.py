# _*_ coding: utf-8 _*_

"""题目：按逗号分隔列表。"""

L = [x for x in range(1,10)]
s = ','.join(str(n) for n in L)
print(s)