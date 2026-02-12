a=int(input())
for i in range(a):
    b, c=input().split()
    try:
        print(int(b)//int(c))
    except (ValueError,ZeroDivisionError) as e:
        print(f"Error Code: {e}")
