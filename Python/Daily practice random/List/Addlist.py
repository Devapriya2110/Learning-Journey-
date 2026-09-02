#Do sum of the two list elements and add in to the third.
n = int(input("Enter no. of elements in list:"))

list1 = []
list2 = []
list3 = []

for i in range (n):
    list1.append(int(input("Enter element list 1 :")))
    
for i in range (n):
    list2.append(int(input("Enter element list 2:")))
    
for i in range (n):
    list3.append(list1[i] + list2[i])
    
print("List 1:",list1)
print("List 2:",list2)
print("List 3:",list3)