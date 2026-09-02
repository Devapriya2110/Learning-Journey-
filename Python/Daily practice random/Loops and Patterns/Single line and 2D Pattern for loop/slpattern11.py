for i in range(1,6):  
    if i==5:
        print(i,"=",sep="",end=" ")
    else:
        print(i,"*",sep="",end=" ")

#Other method
n=int(input("Enter a no:"))
for i in range(1,n+1):
    if i==n:
        print(i,"=",end=" ")
    else:
        print(i,"*",end=" ")
   