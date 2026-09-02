n=int(input("Enter a no:"))
for i in range(1,n+1):
    if i==n:
        print("1/",i," =",sep="",end=" ")
    else:
        print("1/",i," +",sep="",end=" ")