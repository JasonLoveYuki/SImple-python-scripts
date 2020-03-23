s = set([('Adam', 95), ('Lisa', 85), ('Bart', 59)])
for t in s:
	print t[0]+':',t[1]
print 'let us move on'
s= set(['Adam','Lisa','Paul'])
L=['Adam','Lisa','Bart','Paul']
print s
print L
for name in L:
	if name not in s:
		s.add(name)
	else:
		s.remove(name)
print s
print L
