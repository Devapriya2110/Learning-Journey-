'''10. Find Missing Roll Number Task:

-   Store 9 roll numbers in an integer array where the expected roll
    numbers are from 1 to 10.
-   Find and print the missing roll number.'''

roll=[1,2,3,4,5,6,7,8,10]
        
for i in range (1,11):
        if i not in roll:
              print ("Missing No =",i)