a = [
    [10,20,30],
    [40,50,60],
    [70,80,90]
    ]
    
b=[
  [2,20,6],
  [40,9,10],
  [80,90,16]
  ]

common = []
  
for array in a:
    for no in array:
        for arr in b:
            for num in arr:
                if no == num:
                    common.append(no)
                    
print("Common Elements:",common)
        
    
    