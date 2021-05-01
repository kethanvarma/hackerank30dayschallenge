import math
AB = int(input())
BC = int(input())
AC = math.sqrt(AB+BC)
Angle_CAAB = math.degrees(math.atan(AB/BC))
#Angle_ABD = 180-(Angle_ACAB+Angle_ADDB)
print(round(180-Angle_CAAB-90))
