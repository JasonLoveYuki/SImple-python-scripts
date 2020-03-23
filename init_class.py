class Person(object):
	def __init__(self,name,gender,birth,**kw):
		self.name=name
		self.gender=gender
		self.birth=birth
		for k,v in kw.iteritems():
			setattr(self, k, v)
p1=Person('Lily','Male','1770-7-5',interest='football')
print p1.interest
print p1.birth