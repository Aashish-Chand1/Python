#Check whether a triangle is valid or not, when the three angles of the triangle are entered through the keyboard. A triangle is valid if the sum of all the three angles is equal to 180 degrees.
s1 = int(input("Enter 1st side angle:"))
s2 = int(input("Enter 2nd side angle:"))
s3 = int(input("Enter 3rd side angle:"))
ad = s1+s2+s3
if ad==180:
    print("It is an triangle")
else:
    print("It is not an triangle")