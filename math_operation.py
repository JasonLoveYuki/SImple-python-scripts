def gcd(a,b):
	if b==0:
		return a
	else:
		return gcd(b,a%b)
class Rational(object):
	def __init__(self,p,q):
		self.p=p
		self.q=q
	def __add__(self,r):
		return Rational(self.p*r.q+self.q*r.p,self.q*r.q)
	def __sub__(self,r):
		return Rational(self.p*r.q-r.p*self.q,self.q*r.q)
	def __mul__(self,r):
		return Rational(self.p*r.p,self.q*r.q)
	def __div__(self,r):
		return Rational(self.p*r.q,self.q*r.p)
	def __str__(self):
		g=gcd(self.p,self.q)
		return '%s/%s' % (self.p/g,self.q/g)
	__repr__=__str__
	def __int__(self):
		return self.p//self.q
	def __float__(self):
		return float(self.p)/self.q
r1,r2=Rational(1,4),Rational(1,2)
print r1+r2,r1-r2,r1*r2,r1/r2
print int(r1),float(r1)
r3=Rational(6,2)
print int(r3),float(r3)