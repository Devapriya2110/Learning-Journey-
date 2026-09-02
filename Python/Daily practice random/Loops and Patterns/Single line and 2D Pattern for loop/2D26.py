rows = int(input("Enter no of rows: "))
odd_no = int(input("Enter odd no:"))

for i  in range (1,rows+1):
    count = 0
    
    for j in range (odd_no):
        if j%2 != 0:
            print(j,end=" ")
            count +=1
            
            if count == i:
                break      
    print()
            
    