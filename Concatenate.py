import numpy
n,m,p=map(int,input().split())
s=[]
q=[]
for i in range(n):
    s.append(list(map(int,input().split())))
for j in range(m):
    q.append(list(map(int,input().split())))
s=numpy.array(s)
q=numpy.array(q)
result=numpy.concatenate((s,q),axis=0)
print(result)
