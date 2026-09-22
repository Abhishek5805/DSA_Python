
import dis
import math


x1=float(input())
x2=float(input())
y1=float(input())
y2=float(input())

distance=round(math.sqrt((x2-x1)**2+(y2-y1)**2), 2)  #means round the value to 2 decimal places.
print("Euclidean distance between two points is:", distance)