# n=int(input("Enter a no:"))    #if we use range(n)
# for i in range(n):             #it starts indexing from default indexing 0,1,2
    # for j in range(n):
        # print("*",end="")
    # print()
# print("\n")   
n=int(input("Enter a no:")) 
for i in range(1,n+1):      #If we use range(1,n+1) 
    for j in range(1,n+1):
        print("*",end=" ")   #it starts indexing from 1,2,3,4
    print()