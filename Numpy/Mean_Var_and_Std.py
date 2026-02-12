import numpy
a, b=map(int,input().split())
n=[]
for i in range(a):
    n.append(list(map(int,input().split())))
n=numpy.array(n)
print(numpy.mean(n,axis=1))
print(numpy.var(n,axis=0))
print(round(numpy.std(n,axis=None),11))
