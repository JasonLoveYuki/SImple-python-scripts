print map(lambda x :x*x,[1,2,3])
print sorted([1,3,4,2,0],lambda x,y:-cmp(x,y))
myabs=lambda x: -x if x<0 else x
print myabs(-1)
print myabs(10)
def is_not_empty(s):
    return s and len(s.strip()) > 0
print filter(is_not_empty, ['test', None, '', 'str', '  ', 'END'])
print filter(lambda s: s and len(s.strip())>0,['test', None, '', 'str', '  ', 'END'])