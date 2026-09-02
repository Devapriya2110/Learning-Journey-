a = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]
    
a1d = []

a2d = []

#1D Array
for arr in a:
    for no in arr:
        a1d.append(no)
    
print("1D:",a1d)

#2D array
i=0
while i < len(a1d):
    row = []
    
    for j in range(3):
        row.append(a1d[i])
        i+=1
 
    a2d.append(row) 
    
print("2D:",a2d)


    