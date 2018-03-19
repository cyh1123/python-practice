# _*_ coding: utf-8 _*_

"""题目：输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。"""
import re

s = input('input some chars:')
def enum(string):
    letters, space, digit, others = 0, 0, 0, 0
    for i in string:
        if i.isalpha():
            letters += 1
        elif i.isspace():
            space += 1
        elif i.isdigit():
            digit += 1
        else:
            others += 1
    print('char = {0}\nletters = {1}, space = {2}, digit = {3}, others = {4}'.
          format(len(string), letters, space, digit, others))


def regex(string):
    letters = len(re.findall('[a-zA-Z]', string))
    space = len(re.findall(' ', string))
    digit = len(re.findall('\d', string))
    others = len(string) - letters - space - digit
    print('char = {0}\nletters = {1}, space = {2}, digit = {3}, others = {4}'.
          format(len(string), letters, space, digit, others))



enum(s)
regex(s)
