class Person(object):
	def who():
		return 'Person'
class Student(Person):
	def who():
		return 'S'
class Teacher(Person):
	def who():
		return 'T'
class SkillMixin(object):
	pass
class BasketballMixin(SkillMixin):
	def skill(self):
		return 'Basketball'
class FootballMixin(SkillMixin):
	def skill(self):
		return 'Football'
class BStudent(Student,BasketballMixin):
	pass
class FTeacher(Teacher,FootballMixin):
	pass
s=BStudent()
t=FTeacher()
print s.skill()
print t.skill()