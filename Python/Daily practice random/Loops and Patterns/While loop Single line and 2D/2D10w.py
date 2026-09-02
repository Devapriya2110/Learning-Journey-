n=int(input("Enter a no:"))
i=1
mid=(n+1)//2
while i<=n:
    j=1
    while j<=n:
        if i==mid or j==mid:
            print("$",end=" ")
        else:
            print("*",end=" ")
        j+=1
    print()
    i+=1