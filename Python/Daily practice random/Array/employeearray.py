'''1.Reverse Copy of Employee IDs Task:
 - Create an integer array with 10 employee IDs.
 - Copy all elements into another array in reverse order.
 - Print both arrays.'''

employee = [101,102,103,104,105,106,107,108,109,110]
reverse = []

for i in range (9,-1,-1):
    reverse.append(employee[i])

print("Original Array:",employee)
print("\nReversed Array:",reverse)
