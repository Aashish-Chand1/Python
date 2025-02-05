#To create a list of 5 random odd and 4 even number;flattern,sort and print it
import random
lst_even=[]
n = int(input("Enter the range for even:"))
for i in range(n):
    lst1= random.randrange(2,100,2)
    lst_even.append(lst1)
print(lst_even)

lst_odd=[]
m =int(input("Enter the range for odd:"))
for i in range(m):
    lst2= random.randrange(1,100,2)
    lst_odd.append(lst2)
print(lst_odd)

lst_odd[2]=lst_even
print(lst_odd)

fnd_lst=[]
for i in lst_odd:
    print(i)
    if(isinstance(i,list)):
        fnd_lst.extend(i)
    else:
        fnd_lst.append(i)
print(fnd_lst)

