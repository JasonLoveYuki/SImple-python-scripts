d = { 'Adam': 95, 'Lisa': 85, 'Bart': 59, 'Paul': 74 }
sum=0.0
for name,score in d.iteritems():
	print name,':',score
	sum=sum+score
print 'average:',sum/len(d)