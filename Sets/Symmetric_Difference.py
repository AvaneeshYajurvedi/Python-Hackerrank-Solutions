a=int(input())
set1=set(map(int,input().split()))
b=int(input())
set2=set(map(int,input().split()))
result=sorted(set1^set2)
for i in result:
    print (i)
