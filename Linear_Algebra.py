import numpy
a=int(input())
n=[]
for i in range(a):
    n.append(list(map(float,input().split())))
n=numpy.array(n)
print(numpy.linalg.det(n))
