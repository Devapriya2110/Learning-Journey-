n=int(input("Enter a no:"))
i=1
while i<=n:
    j=1
    while j<=n:
        if i==j:
            print("$",end=" ")
        else:
            print("*",end=" ")
        j+=1
    print()
    i+=1
            