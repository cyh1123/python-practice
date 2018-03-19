# _*_ coding: utf-8 _*_

"""题目：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？"""

# num+100=n**2    i+100+168=m**2
# (m-n)(m+n)=168
# i=m-n j=m+n
# i,j 为偶数，同号
# 讨论i，j正负无意义，m = (i + j) / 2，归结为求m**2


for i in range(1, 85):
    if 168 % i == 0:
        j = 168 / i
        if i > j and (i + j) % 2 ==0 and (i - j) % 2 == 0:
            m = (i + j) / 2
            n = (i - j) / 2
            print('m:%s, n:%s' % (m ,n))
            print('this number is :%s\n' % (n**2 - 100))
