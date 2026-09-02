'''4.  Common Customers Task:

-   Create two integer arrays of size 10.
-   Find the common elements.
-   Copy them into a third array.
-   Print the common elements.'''

a1 = [1,10,100,600,800,80,25,30,60,550]
a2 = [10,600,50,83,73,123,190,100,60,2]
common = []

for i in range (10):
    for j in range(10):
        if a1[i]==a2[j]:
            common.append(a1[i])
            break
            
print("Array 1:",a1)
print("Array 2:",a2)
print("Common Elements:",common)