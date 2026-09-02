n=int(input("Enter a no:"))
i=1
while(i<=n):
    if i==n:
        print("1/",i,"=",sep="",end=" ")
    else:
        print("1/",i,"+",sep="",end=" ")
    i+=1