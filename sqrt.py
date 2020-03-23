# -*- coding=utf-8 -*-
#函数式编程特点：把计算视作函数；纯函数式编程不需要变量；支持高阶函数
#python支持的函数式编程特点：不是纯函数式编程，允许有变量；支持高阶函数；支持闭包，能返回函数；有限度支持匿名函数
#变量可以指向函数：f=abs 对f进行调用和对abs调用一样
#函数名就是指向函数的变量 abs=len abs就指向了len
#高阶函数=能接受函数作为变量的函数
import math
def add(x,y,f):
	return f(x)+f(y)
print add(1,2,math.sqrt)