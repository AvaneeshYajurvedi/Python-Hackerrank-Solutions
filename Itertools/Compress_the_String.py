from itertools import groupby
a=input()
for key,group in groupby(a):
    s=list(group).count(key),int(key)
    print(tuple(s),end=" ")
