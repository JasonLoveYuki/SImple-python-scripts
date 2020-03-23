# -*- coding=utf-8 -*-
list=['abc',1,'Ac',('a',1)]
def up(l):
	 return [x.upper() for x in list if isinstance(x,str)==True]
#上面的==True可以去掉
print up(list)