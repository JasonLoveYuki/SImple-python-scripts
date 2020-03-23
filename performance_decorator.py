import time,functools
def performance(prefix):
	def performance_decorator(f):
		@functools.wraps(f)
		def wrapper(*args,**kw):
			t1=time.time()
			r=f(*args,**kw)
			t2=time.time()
			def rate(prefix):
				if prefix=='s':
					return 1
				if prefix=='ms':
					return 100
				return 'error'
			print'call %s in %f%s'%(f.__name__,(t2-t1)*rate(prefix),prefix)
			return r
		return wrapper
	return performance_decorator

@performance('s')
def factorial(n):
    return reduce(lambda x,y: x*y, range(1, n+1))
print factorial(10)
