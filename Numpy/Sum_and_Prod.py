import numpy
a, b=map(int,input().split())
n=[]
for i in range(a):
    n.append(list(map(int,input().split())))
n=numpy.array(n)
m=numpy.sum(n,axis=0)
print(numpy.prod(m))
