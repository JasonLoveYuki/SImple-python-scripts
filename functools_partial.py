import functools
int2=functools.partial(int,base=2)
print int2('10')
def cmp_ignore_case(x,y):
	s1=x.upper()
	s2=y.upper()
	if s1<s2:
		return -1
	if s1>s2:
		return 1
	return 0
print sorted(['bob','about','Zoo','CrediT'],cmp_ignore_case)
sorted_ignore_case=functools.partial(sorted,cmp=lambda s1,s2:cmp(s1.upper(),s2.upper()))
print sorted_ignore_case(['bob','about','Zoo','CrediT'])