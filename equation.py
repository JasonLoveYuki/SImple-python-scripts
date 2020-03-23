import math
def answer(a,b,c):
	x1=(-b+math.sqrt(b*b-4*a*c))/(2*a)
	x2=(-b-math.sqrt(b*b-4*a*c))/(2*a)
	return x1,x2
x=answer(1,2,1)
print x