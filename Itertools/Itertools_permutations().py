from itertools import permutations
a, b=input().split()
a=sorted(ch for ch in a if ch.isalpha())
b=int(b)
for p in permutations(a,b):
    print(''.join(p))
