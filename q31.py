# _*_ coding: utf-8 _*_

"""题目：请输入星期几的第一个字母来判断一下是星期几，如果第一个字母一样，则继续判断第二个字母。"""


def identify():
    letter = input('input letter step by step: ')
    week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    def pick(letter, week, n):
        days = []
        for d in week:
            if letter.lower() == d[n].lower():
                days.append(d)
        if len(days) == 0:
            print('wrong letter! restart the program')
            return identify()
        if len(days) == 1:
            return days[0]
        letter2 = input('input one more letter: ')
        return pick(letter2, days, n+1)
    return pick(letter, week, 0)


print(identify())