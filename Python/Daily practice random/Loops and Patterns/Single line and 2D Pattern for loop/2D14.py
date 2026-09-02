n=int(input("Enter no:"))
temp=1
for i in range(1,n+1):
    for j in range(1,n+1):
        print(temp,end=" ")
        temp+=1
    print()