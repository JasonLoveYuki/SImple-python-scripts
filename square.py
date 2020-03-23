# -*- coding=utf-8 -*-
#下面是一种做法
#print[x*x for x in range(1,20) if x*x<101]
#下面是错误做法，原因是math.sqrt返回浮点数
#import math
#def square(x):
#	return isinstance(math.sqrt(x),int)
#print filter(square,range(1,101))
import math
def square(x):
	r=int(math.sqrt(x))
	return not(x-r*r)
#或者return x==r*r
print filter(square,range(1,101))