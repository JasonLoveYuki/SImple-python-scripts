# -*- coding: utf-8 -*-
#通过 or 运算，可以把空字符串“变成”默认字符串，而非空字符串保持不变。
a= 'python'
print 'hello', a or 'zero'
a= ''
print 'hello', a or 'zero'