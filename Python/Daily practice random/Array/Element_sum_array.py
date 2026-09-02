a = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]

#Sum of row elements  
print("Sum of row elements:") 
for arr in a:
    total = 0
    
    for no in arr:
        total+= no
        
print(total)
  
#Sum of column elements
print("\nSum of column elements:")
for j in range(3):
    total = 0
    
    
    for i in range(3):
        total += a[i][j]
        
    print(total)
    
#Sum of diagonal elements
diagonal1 = 0
diagonal2 = 0

for i in range(3):
    diagonal1 += a[i][i]
    diagonal2 += a[i][2-i]

print("\nFirst diagonal:", diagonal1)
print("Second diagonal:", diagonal2)    
    
# Sum of cross elements
cross = diagonal1 + diagonal2 - a[1][1]

print("Sum of cross elements:", cross)        
        
    