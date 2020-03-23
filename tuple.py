# -*- coding:utf-8 -*-
#tuple 和 list 非常类似，但是，tuple一旦创建完毕，就不能修改了
t=('a','b','c','d')
print t
a=(1,)
print a
b=('adam',)
print b
#tuple所谓的“不变”是说，tuple的每个元素，指向永远不变。
#即指向'a'，就不能改成指向'b'，指向一个list，就不能改成指向其他对象，但指向的这个list本身是可变的！
c=(1,2,[3,4])
L=c[2]
L[0]='x'
print c
print c[2]
d=('a','b',['A','B'])
print d
d2=('a','b',('A','B'))
L2=d2[2]
print L2
#L2不能改动