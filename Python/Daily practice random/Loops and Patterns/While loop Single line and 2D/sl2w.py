n=int(input("Enter no :"))
i=1
mid=(n+1)//2
while(i<=n):
    if i == mid:
        print("$",end=" ")
    else:
        print("*",end=" ")
    i+=1