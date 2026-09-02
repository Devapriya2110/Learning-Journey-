n=int(input("Enter a no:"))
i=1
total=0
while(i<=n):
    total+=i
    if i==n:
        print(i,"=",total,end=" ")
    else:
        print(i,"+",end=" ")
    i+=1
    

    
    