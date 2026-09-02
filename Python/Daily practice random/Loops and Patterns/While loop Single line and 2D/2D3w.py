n = int(input("Enter the size: "))
i=1
while i <= n:
    j = 1
    while j <= n:
        if j==1 or j==n:
            print("$",end=" ")
        else:
            print("*", end=" ")
        j += 1
    print()
    i += 1