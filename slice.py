# -*- coding=utf-8 -*-
#1-100的数
L=range(1,101)
#输出1-10
print L[:10]
#输出3的倍数
print L[2:99:3]
#输出3的倍数
print L[2::3]
print L[4:50:5]

l=range(1,101,1)
#倒序切片包含起始索引，不包含结束索引
print l[-10:]
#要包含最后一个数就不写结束索引
print l[-46::5]

def Big(str):
	return str[:1].upper()+str[1:]
print Big('yuki')
print Big('iamhappy')