# _*_ coding: utf-8 _*_

"""题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？"""

def route(high, time):
    s = - high
    for i in range(0, time):
        high /= 2
        s += 4 * high
    return s, high

print(route(100, 10))
