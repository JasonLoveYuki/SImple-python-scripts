# -*- coding:utf-8 -*-
#用 for 循环或者 while 循环时，如果要在循环体内直接退出循环，可以使用 break 语句。
#break退出循环的条件是循环已执行了20次
x=1
N=0
sum=0
while True:
	sum=sum+x
	x=2*x
	N=N+1
	if N>=20:
		break
print sum