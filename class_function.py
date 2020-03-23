# -*-coding=utf-8 -*-
class Person(object):
	def __init__(self,name,score):
		self.name=name
		self.__score=score
	def get_grade(self):
		if self.__score>=80:
			return 'A-优秀'
		elif self.__score>=60:
			return 'B-及格'
		return 'C-不及格'
p1=Person('Bob',99)
print p1.get_grade()
p1=Person('Bobb',70)
print p1.get_grade()
p1=Person('Bobbb',9)
print p1.get_grade()



