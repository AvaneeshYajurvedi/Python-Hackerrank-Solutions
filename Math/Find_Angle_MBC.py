import math
AB=float(input())
BC=float(input())
c=math.atan2(AB,BC)
d=round(math.degrees(c))
print(str(d)+chr(176))
