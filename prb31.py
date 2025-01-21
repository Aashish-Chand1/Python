#Accept a year value from the user. Check whether it is a leap year or not
yr = int(input("Enter any year:"))
if (yr % 4 ==0 and yr%100 != 0):
    print(yr,"is leap a year")
else:
    print(yr,"is not a leap year")