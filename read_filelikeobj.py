import json
class File_like(object):
	def __init__(self,s):
		self.s=s
	def read(self):
		return self.s
f=File_like(r'["Tim","Bob","Alice"]')
print json.load(f)