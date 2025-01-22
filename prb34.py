#Given the length and breadth of a rectangle, write a program to find whether the are of the rectangle is greater than its perimeter.
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
perimeter = 2 * (length + breadth)

if area > perimeter:
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than area")


