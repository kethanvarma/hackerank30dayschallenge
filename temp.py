import math
AB = int(input())
BC = int(input())
AC = math.sqrt(AB+BC)

#formula to find out angles of traingle by using tregnometry
Angle_CAAB = math.degrees(math.atan(AB/BC))
print(round(180-Angle_CAAB-90))
