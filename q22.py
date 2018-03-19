# _*_ coding: utf-8 _*_

"""题目：两个乒乓球队进行比赛，各出三人。甲队为a,b,c三人，乙队为x,y,z三人。已抽签决定比赛名单。有人向队员打听比赛的名单。a说他不和x比，c说他不和x,z比，请编程序找出三队赛手的名单。"""
import itertools

t1 = ['a', 'b', 'c']
t2 = ['x', 'y', 'z']
perm = itertools.permutations(t2)

for p in perm:
    flag = 0
    for i in zip(t1, p):
        if i in [('a', 'x'), ('c', 'x'), ('c', 'z')]:
            flag = 1
            break
    if not flag:
        for x in zip(t1, p):
            print('%s V.S. %s' % x)
        break