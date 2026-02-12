import numpy
a=int(input())
n=[]
m=[]
for i in range(a):
    n.append(list(map(int,input().split())))
for i in range(a):
    m.append(list(map(int,input().split())))
n=numpy.array(n)
m=numpy.array(m)
print(numpy.dot(n,m))
