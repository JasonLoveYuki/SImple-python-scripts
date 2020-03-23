# -*-coding:utf-8 -*-
#在循环过程中，可以用break退出当前循环，还可以用continue跳过后续循环代码，继续下一次循环。
sum=0
x=0
while True:
	x=x+1
#break，不然要多加101
	if x>100:
		break
	if x%2==0:
		continue
	sum=sum+x
print sum
