def calc_prod(lst):
	def lazy_calc_prod():
		def prod(x,y):
			return x*y
		return reduce(prod,lst)
	return lazy_calc_prod
f=calc_prod([1,2,3,4])
print f()