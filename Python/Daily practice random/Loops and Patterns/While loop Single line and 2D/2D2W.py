n = int(input("Enter the size: "))
mid=(n+1)//2
i=1
while i <= n:
    j = 1
    while j <= n:
        if j==mid:
            print("$",end=" ")
        else:
            print("*", end=" ")
        j += 1
    print()
    i += 1