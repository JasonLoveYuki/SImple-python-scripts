class Fib(object):
	def __call__(self,num):
		a,b=0,1
		L=[0]
		for n in range(0,num):
			L.append(a)
			a,b=b,a+b
		self.list=L		
		print L
f=Fib()
print f(10)
