a=int(input("Enter a no a:"))
b=int(input("Enter a no b:"))
c=int(input("Enter a no c:"))
d=int(input("Enter a no d:"))
if a>b:
    if a>c:
        if a>d:
            print("The maximum no is",a)
else:
    if b>c:
        if b>d:
            print("The maximum no is",b)
    else:
        if c>a:
            if c>b:
               if c>d:
                    print("The maximum no is",c)
               else:
                    print("The maximum no is:",d)
            