from itertools import combinations
a, b=input().split()
b=int(b)
a=sorted(list(a.upper()))
s=[]
for i in range(1,b+1):
    s.extend(sorted(list(combinations(a,i))))
for n in s:
    print("".join(n))
