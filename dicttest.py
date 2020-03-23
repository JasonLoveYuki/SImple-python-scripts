# -*- coding=utf-8 -*-
#作为 key 的元素必须不可变，list是可变的，就不能作为 key。
d={
	(1,2,['a','b']):'Adam'
}
print d