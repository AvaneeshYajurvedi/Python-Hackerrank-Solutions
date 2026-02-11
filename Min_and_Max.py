import numpy 
a, b=map(int,input().split())
n=[]
for i in range(a):
    n.append(list(map(int,input().split())))
n=numpy.array(n)
m=numpy.min(n,axis=1)
print(numpy.max(m))
