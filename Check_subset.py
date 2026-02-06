q=int(input())
for i in range(q):
    a=int(input())
    s=set(map(int,input().split()))
    b=int(input())
    m=set(map(int,input().split()))
    print(s.issubset(m))
