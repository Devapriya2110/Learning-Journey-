n=int(input("Enter the no:"))
mid = (n+1)//2                           #If we use range(1,n+1) 
for i in range(1,n+1):        #it starts indexing from 1,2,3,4
    for j in range(1,n+1):
        if j == mid:
            print("$",end="")
        else:
            print("*",end="")
    print()
# print("\n")    
# for i in range(n):       #if we use range(n)
    # for j in range(n):   #it starts indexing from default indexing 0,1,2
        # if j==2:
            # print("$",end="")
        # else:
            # print("*",end="")
    # print()
    