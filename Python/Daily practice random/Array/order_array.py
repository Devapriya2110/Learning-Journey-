'''9.Count Duplicate Orders Task:

-   Create an integer array with 10 order IDs.
-   Count the occurrence of each duplicate value.
-   Print each duplicate value with its occurrence count.'''

a = [101,102,103,102,103,109,110]
b = []

for i in range(len(a)):
    for j in range(len(a)):
        if a[i] == a[j]:
                for z in b:
                    if z == a[j]:
                        break
                    b.append(a[i])
                print(f"value  = {a[i]} || count = {a.count(a[i])}")
                
