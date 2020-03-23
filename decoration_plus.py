import time
def log(f):
	def fn(*args,**kw):
		print 'call:'+f.__name__+'()...'
		return f(*args,**kw)
	return fn
@log
def add(x,y):
	return x+y
print add(2,3)
def performance(f):
	def fn(*args,**kw):
		t1=time.time()
		r=f(*args,**kw)
		t2=time.time()
		print 'call %s() in %f'%(f.__name__,(t2-t1))
		print 'call '+f.__name__+'() in '+ str(t2-t1)
		return r
	return fn
@performance
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)