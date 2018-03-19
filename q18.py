# _*_ coding: utf-8 _*_

"""题目：求s=a+aa+aaa+aaaa+aa...a的值，其中a是一个数字。例如2+22+222+2222+22222(此时共有5个数相加)，几个数相加由键盘控制。"""

a = int(input('input base number: '))
n = int(input('input control number: '))
s = 0
assert 1
for i in range(1, n+1):
    s += a * i * 10**(n-i)
print(s)

