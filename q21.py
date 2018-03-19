# _*_ coding: utf-8 _*_

"""题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。"""
import itertools

def allpeach(remain, days):
    def eatpeach(total, days):
        remain = total/2 - 1
        if days == 1:
            return remain
        return eatpeach(remain, days - 1)

    for i in itertools.count():
        if eatpeach(remain, days) == 1:
            print(i)
            break



def allpeach2(remain, days):
    for day in range(0, days):
        a = 2 * (remain + 1)
        remain = a
    return remain

print(allpeach2(1, 9))
