for i in range(1,6):   
    if i==1 or i==5:
        print("$",end=" ")
    else:
        print("*",end=" ")
        
#Other method
n= int(input("Enter a no:"))
for i in range(1,n+1):
    if i in range(1,n+1,4):
        print("$",end=" ")
    else:
        print("*",end=" ")
   