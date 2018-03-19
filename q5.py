# _*_ coding: utf-8 _*_

"""题目：输入三个整数x,y,z，请把这三个数由小到大输出。"""

# 造造轮子
# 不造轮子用sort

l = []
for i in range(3):
    a = (float(input("input number %s..." % (i + 1))))
    if len(l) == 0:
        l.append(a)
    else:
        for m, n in enumerate(l):
            # enumerate 为动态函数，只要l更新，(m,n)也不停更新
            if a <= n:
                l.insert(m, a)
                break
            else:
                l.append(a)
                break
print(l)




