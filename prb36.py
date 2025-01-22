#Given the coordinates (x,y) of center of a circle and its radius, determine whether a point lies inside the circle, on the circle or outside the circle. (Hint: Use sqrt( ), pow( ) )
import math
xc,yc = map(float,input("Enter the centre of the circle:").split())
r = float(input("Enter the radius os the circle:"))
xp,yp = map(float,input("Enter the points on the circle:").split())
d = math.sqrt(math.pow(xp-xc,2)+ math.pow(yp-yc,2))

if d<r:
    print("These points are inside the circle")
elif d==r:
    print("These points are on the circle")
else:
    print("These points are outside the circle")