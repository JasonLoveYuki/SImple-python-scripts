# -*- coding=utf-8 -*-
l=[]
a=1
n=100
while True:
	if a>n:
		break
	l.append(a*a)
	a=a+1
print l
#sum()函数接受一个list作为参数，并返回list所有元素之和
print sum(l)