class Person(object):
	__count=0
	def __init__(self,name):
		self.name=name
		Person.__count=Person.__count+1
		print Person.__count
p1=Person('Bob')
p2=Person('Adam')
print Person.__count