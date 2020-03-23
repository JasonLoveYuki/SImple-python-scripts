# -*- coding=utf-9 -*-
#比较函数的定义是，传入两个待比较的元素 x, y，如果 x 应该排在 y 的前面，返回 -1，如果 x 应该排在 y 的后面，返回 1。如果 x 和 y 相等，返回 0
def quene(x,y):
	if x.upper()<y.upper():
		return -1
	if x.upper()>y.upper():
		return 1
	return 0
print sorted(['bob', 'about', 'Zoo', 'Credit'],quene)