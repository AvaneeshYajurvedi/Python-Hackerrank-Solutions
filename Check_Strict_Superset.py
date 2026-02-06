a=set(map(int,input().split()))
b=int(input())
result=True
for i in range(b):
    q=set(map(int,input().split()))
    if not a.issuperset(q):
        result=False
print(result)
