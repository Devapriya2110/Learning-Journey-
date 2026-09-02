n=int(input("Enter no :"))
i=1
while(i<=n):
    if i==1 or i==n:
        print("$",end=" ")
    else:
        print("*",end=" ")
    i+=1