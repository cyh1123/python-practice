# _*_ coding: utf-8 _*_

"""题目：打印出如下图案（菱形）:

   *
  ***
 *****
*******
 *****
  ***
   *
"""

def diamond(n):
    for i in range(1, 2*n):
        print(' ' * abs(i - n) + '*' * (2 * (n - abs(i -n)) -1))


diamond(7)