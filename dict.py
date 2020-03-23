# -*- coding=utf-8 -*-
#花括号 {} 表示这是一个dict，然后按照 key: value, 写出来即可
d={
'Adam':95,
'Lisa':85,
'Bart':59,
'Paul':75
}
if 'Adam' in d:
	print 'Adam:',d['Adam']
print 'Lisa:',d.get('Lisa')
print 'Bart:',d.get('Bart')
print d.get('John')
if 'John' in d:
	print d['John']
print d