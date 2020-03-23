# -*- coding=utf-8 -*-
#对于复杂的表达式，可以引入函数
d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59 }
def complex(x,y):
	if y<60:
		return x,'fail'
	return x,'ok'
print [complex(name,score) for name,score in d.iteritems()]