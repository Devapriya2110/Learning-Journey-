'''8.  Merge Daily Orders Task:

-   Create two integer arrays of size 10.
-   Merge both arrays into a third array of size 20.
-   Print the merged array.'''

a1 = [1,2,3,4,5,6,7,8,9,10]
a2 = [10,20,30,40,50,60,70,80,90,100]
a3 = []

a3=a1+a2

print("Array 1:",a1)
print("Array 2:",a2)
print("Merged Array:",a3)

#Another method
a1 = [1,2,3,4,5,6,7,8,9,10]
a2 = [10,20,30,40,50,60,70,80,90,100]
a3 = []

for i in range (10):
        a3.append(a1[i])

for i in range (10):
       a3.append(a2[i])

print("Merged Array",a3)