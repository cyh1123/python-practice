# _*_ coding: utf-8 _*_

"""题目：输入某年某月某日，判断这一天是这一年的第几天？"""

def leapyear(y):
    assert y > 0 and isinstance(y, int)
    if (y % 400 == 0) or (y % 100 != 0 and y % 4 == 0):
        return True
    else:
        return False

def days():
    mydate = input("input date (YYYYMMDD): ")
    assert int(mydate), 'wrong form!'
    daysofmonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year, month, day = map(int, [mydate[0:4], mydate[4:6], mydate[6:8]])
    if leapyear(year):
        daysofmonths[1] = 29
    assert year > 0 and 0 < month < 13 and 0 < day <= daysofmonths[month-1], 'wrong date!'
    ans = sum(daysofmonths[:month-1]) + day
    print(ans)

days()
