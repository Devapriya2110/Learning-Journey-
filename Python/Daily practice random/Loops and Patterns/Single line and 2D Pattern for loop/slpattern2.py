for i in range(1,6):   
    if i == 3:
        print("$",end=" ")
    else:
        print("*",end=" ")
        
#Other method by taking user input
n= int(input("Enter a no:"))
for i in range(1,n+1):
    if i == (n+1)//2:
        print("$",end=" ")
    else:
        print("*",end=" ")
   
