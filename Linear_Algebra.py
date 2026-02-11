import numpy
a=int(input())
n=[]
for i in range(a):
    n.append(list(map(float,input().split())))
n=numpy.array(n)
print(round(numpy.linalg.det(n), 2))
