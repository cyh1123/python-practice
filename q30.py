# _*_ coding: utf-8 _*_

"""题目：一个5位数，判断它是不是回文数。即12321是回文数，个位与万位相同，十位与千位相同。"""

def recognize(num):
    n = str(num)
    assert len(n) > 1, 'wrong number'
    def run(n):
        if len(n) == 1:
            return True
        if n[0] != n[-1]:
          return False
        return run(n[1:-1])
    return run(n)

print(recognize(12321))

