class Fib(object):
	def __init__(self,n):
		a=0
		b=1
		L=[]
		for k in range(0,n):
			L.append(a)
			a,b=b,a+b
		self.list=L
	def __str__(self):
		return str(self.list)
	__repr__=__str__
	def __len__(self):
		return len(self.list)
p=Fib(10)
print p
print len(p)
