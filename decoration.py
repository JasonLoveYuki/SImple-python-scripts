def new_f1(f):
	def fk(x):
		print 'call'+f.__name__+'()'
		return f(x)
	return fk
@new_f1
def f1(x):
	return x+1
print f1(4)
print f1(2)
print f1(3)
print f1(4)