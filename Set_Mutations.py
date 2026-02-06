a=int(input())
b=set(map(int,input().split()))
n=int(input())
for i in range(n):
    cmd=input().split()
    q=set(map(int,input().split()))
    if cmd[0]=='intersection_update':
        b.intersection_update(q)
    elif cmd[0]=='update':
        b.update(q)
    elif cmd[0]=='difference_update':
        b.difference_update(q)
    elif cmd[0]=='symmetric_difference_update':
        b.symmetric_difference_update(q)
print(sum(b))        
