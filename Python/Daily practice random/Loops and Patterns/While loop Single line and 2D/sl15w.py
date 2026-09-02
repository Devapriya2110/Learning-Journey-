n=int(input("Enter a no:"))
i=1
while(i<=n):
    if i==n:
        print(i,"=",end=" ")
    elif i%2 == 0:
        print(i,"+",end=" ")
    else:
        print(i,"-",end=" ")
    i+=1
#for sum
n=int(input("Enter a no:"))
i=1
total=0
while(i<=n):
    if i%2==0:
        total-=i
    else:
        total+=i
    
    if i==n:
        print(i,"=",end=" ")
    elif i%2 == 0:
        print(i,"+",end=" ")
    else:
        print(i,"-",end=" ")
    i+=1    
print(total)   