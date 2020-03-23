
# -*-coding=utf-8 -*-
d={
	95:'Adam',
	85:'Lisa',
	59:'Bart'
}
d[72]='Bart'
print d
for key in d:
#TypeError: unsupported operand type(s) for +: 'int' and 'str'
#加号可用在字符串之前没有空格
	print key,':',d[key]