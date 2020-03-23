# -*- coding=utf-8 -*-
#请定义一个 greet() 函数，它包含一个默认参数，如果没有传入，打印 'Hello, world.'，如果传入，打印 'Hello, xxx.'
#def greet(x,n=1):
#	if n=1:
#		print 'Hello, world'
#		return
#	else:
#		print 'Hello, xxx'
#		return
#greet(1,2)
#greet(1)
#greet(1,1)
def greet(name='world'):
	print 'Hello,',name+'.'
greet()
greet('Jason')