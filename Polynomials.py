import numpy
a=list(map(float,input().split()))
b=int(input())
a=numpy.array(a)
print(numpy.polyval(a,b))
