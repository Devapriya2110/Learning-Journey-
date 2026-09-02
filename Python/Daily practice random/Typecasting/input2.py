a=input("Enter first no:")
b=input("Enter second no:")
c=input("Enter third no:")
print(type(a))
print(type(b))
print(type(c))
a=int(a)
print(type(a))
b=int(b)
print(type(b))
c=int(c)
print(type(c))

d=a
a=b
b=c
c=d
print("Swapped a:",a)
print("Swapped b:",b)
print("Swapped c:",c)


