# _*_ coding: utf-8 _*_

"""题目：将一个列表的数据复制到另一个列表中。"""
# 深拷贝、浅拷贝


a = [1, 1, 2, 3, 5, 8]
print('a =%s ID(a):%s' % (a,id(a)))
b = a
# 将a的内存地址复制给b
print('b =%s ID(b):%s' % (b,id(b)))
c = a[:]
# 将a的内容复制给c
print('c =%s ID(c):%s\n' % (c,id(c)))

a[0] = 0
# a在原内存地址上修改内容
print('a =%s ID(a):%s' % (a,id(a)))

print('b =%s ID(b):%s' % (b,id(b)))
# b跟着a变化
print('c =%s ID(c):%s\n' % (c,id(c)))


