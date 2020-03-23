# -*- coding=utf-8 -*-
class Student(object):
	def __init__(self,name,score):
		self.name=name
		self.score=score
	def __str__(self):
		return '(%s, %s)'%(self.name,self.score)
	__repr__=__str__
	def __cmp__(self,s):
		if self.score>s.score:
			return -1
		elif self.score<s.score:
			return 1
		elif self.name<self.name:
			return -1
		elif self.name>self.name:
			return 1
		else:
			return 0
#方法跑通了，但是很丑陋，简单方法如下：
#    def __cmp__(self,s):
#        if self.score==s.score:
#            return cmp(self.name,s.name)
#        return -cmp(self.score,s.score)
L=[Student('Adam',99),Student('Ann',99),Student('Bob',60),Student('Anna',79),Student('Jason',100)]
print sorted(L)