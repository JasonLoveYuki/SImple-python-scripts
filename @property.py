class Student(object):
    def __init__(self, name, score):
        self.name = name
        self.__score = score
    @property
    def score(self):
        return self.__score
    @score.setter
    def score(self, score):
        if score < 0 or score > 100:
            raise ValueError('invalid score')
        self.__score = score 
    @property
    def garde(self):
    	if self.__score<60:
    		return 'C'
    	if self.score<80:
    		return 'B'
    	return 'A'
#    def get_score(self):
#        return self.__score
#    def set_score(self, score):
#        if score < 0 or score > 100:
#            raise ValueError('invalid score')
#        self.__score = score
s1=Student('Bob',50)
print s1.garde
s1.score=60
print s1.score
print s1.garde
s1.score=99
print s1.score
print s1.garde