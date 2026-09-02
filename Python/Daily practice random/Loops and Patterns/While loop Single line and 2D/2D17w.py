n=int(input("Enter a no:"))
i=1
while i<=n:
    j=1
    while j<=n:
        if (i+j)%2 == 0:
            print(1,end=" ")
        else:
            print(0,end=" ")
        j+=1
    print()
    i+=1