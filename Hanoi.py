# -*-coding=utf-8 -*-
#def move(n,a,b,c):
#	if n==1:
#		return a,'-->',c
#	move(n-1,a,c,b)
#	a,'-->',c
#	move(n-1,b,a,c)
#print move(4,'A','B','C）

#在交互模式下，return的结果会自动打印出来，而作为脚本单独运行时则需要print函数才能显示。

def move(n,a,b,c):
	if n==1:
		print a,'-->',c
		return
	move(n-1,a,c,b)
	print a,'-->',c
	move(n-1,b,a,c)
move(2,'A','B','C')