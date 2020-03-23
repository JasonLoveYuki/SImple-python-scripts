A=[1,2,3,4,5,6,7,8,9]
B=[0,1,2,3,4,5,6,7,8,9,0]
C=B
print [100*a+10*b+c for a in A for b in B for c in C if a==c]