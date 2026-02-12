n = int(input())
s = set(map(int, input().split()))
b=int(input())
i=1
while i<=b:
    data=input().split()
    if data[0]=='pop':
        s.pop()
    elif data[0]=='remove':
        ele=int(data[1])
        s.remove(ele)
    elif data[0]=='discard':
        ele=int(data[1])
        s.discard(ele)
    i+=1
print(sum(s))
