#Print largest and smallest values out of three.
a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
c = int(input("Enter 3rd number:"))
if a>b and a>c:
    print(a,"is the greatest")
elif b>a and b>c :
    print(b,"is the greatest")
else:
    print(c,"is the greatest")

if a<b and a<c:
    print(a,"is the smallest")
elif b<a and b<c :
    print(b,"is the smallest")
else:
    print(c,"is the smallest")