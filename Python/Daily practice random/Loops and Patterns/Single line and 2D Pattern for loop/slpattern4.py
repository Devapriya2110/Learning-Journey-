for i in range(1,7):  
    if i in range(1,7,2):
        print("$",end=" ")
    else:
        print("*",end=" ")

#OTHER METHOD
n= int(input("Enter a no:"))
for i in range(1,n+1):
    if i%2!=0 :
        print("$",end=" ")
    else:
        print("*",end=" ")
   