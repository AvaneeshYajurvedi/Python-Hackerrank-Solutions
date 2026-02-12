import numpy
n,m=map(int,input().split())
rows=[]
for i in range(n):
    rows.append(list(map(int,input().split())))
s=numpy.array(rows)
print(numpy.transpose(s))
print(s.flatten())
