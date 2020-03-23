def up(name):
	return name[0].upper()+name[1:].lower()
l=['adam','LISA','barT']
print map(up,l)