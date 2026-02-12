a=int(input())
set1=set(map(int,input().split()))
b=int(input())
set2=set(map(int,input().split()))
result=set1-set2
l=len(result)
print(l)
