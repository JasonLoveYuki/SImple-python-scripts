class Person(object):
	def __init__(self,name,score):
		self.name=name
		self.__score=score
p=Person('yang',100)
print p.__score