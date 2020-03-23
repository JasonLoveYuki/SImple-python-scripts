# -*- coding=utf-8-*-
#每个tuple元素都包含两个元素，for循环又可以进一步简写成index和name
rank=range(1,5)
L=['Adam','Lisa','Bart','Paul']
for s in zip(rank,L):
	print s[0],'-',s[1]