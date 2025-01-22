#Given three points (x1,y1), (x2,y2) and (x3,y3), check if all the three points fall on one straight line.
x1,y1 = map(float,input("Enter the value of x1,y1:").split())
x2,y2=map(float,input("Enter the value of x2,y2: ").split())
x3,y3 = map(float,input("Enter the value of x3,y3:").split())

if (x2 - x1) == 0 and (x3 - x2) == 0:
     print(True)  
elif (x2 - x1) == 0 or (x3 - x2) == 0:
     print(False) 

m1 = (y2-y1)/(x2-x1)
m2 = (y3-y2)/(x3-x2)

if m1==m2:
    print("The points are colinear and fall on same line")
else:
    print("The points are not colinear and not fall on line")