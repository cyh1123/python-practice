# _*_ coding: utf-8 _*_

"""题目：古典问题：有一对兔子，从出生后第3个月起每个月都生一对兔子，小兔子长到第三个月后每个月又生一对兔子，假如兔子都不死，问每个月的兔子总数为多少？"""

def fib():
    a, b = 0, 1
    while True:
        a, b = b, a + b
        yield a

fib = fib()
def run(lim):
    n = 1
    for i in fib:
        print('第%s个月，共有%s对兔子...' % (n, i))
        n += 1
        if n > lim:
            break

run(10)