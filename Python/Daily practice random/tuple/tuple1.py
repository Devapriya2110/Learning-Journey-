a = (90,80,90,120,100,120)
for i in dir(a):
    if "_" not in i:
        print(i)
#No. of total elements        
print("No. of elements:",len(a))
#Counting element occurence
print("Count of element:",a.count(90))
#Index
print("Value at index 3:",a[3])
print("Index of 120:",a.index(120))
    
