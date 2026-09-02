n=int(input("Enter a no:"))
mid=(n+1)//2
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==mid:
            print("$",end="")
        else:
            print("*",end="")
    print()