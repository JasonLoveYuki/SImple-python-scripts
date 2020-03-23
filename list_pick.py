# -*- coding=utf-8 -*-
L=[1,2,3,4,5,6,7,8,9]
N=[]
n=5
while n>0:
	k=5-n
	N.append(L[k])
	n=n-1
#更简单的方法是用range(n)和针对list的for
print N