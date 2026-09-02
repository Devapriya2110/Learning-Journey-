n=int(input("Enter a no:"))   
for i in range(1,n+1):
    if i==n:
        if n%2==0:
            print("+",i,"=",end="")
        else:
            print("-",i,"=",end="")
    elif i%2==0 :
        print("+",i,end="")
    else:
        print("-",i,end="")
        