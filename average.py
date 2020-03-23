def average(*args):
	if len(args)==0:
		print 0
		return
	sum=0.0
	n=0
	for elements in args:
		sum=sum+elements
	return sum/len(args)
print average(1,2,3)
print average(1,2)
print average()