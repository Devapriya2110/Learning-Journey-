#Create two list and copy both the list in third list.
n1 = int(input("Enter no. of elements in list1:"))
list1=[]

for i in range (n1):
    list1.append(int(input("Enter element:")))
    
n2 = int(input("Enter no. of elements in list2:"))   
 
list2=[]    
for i in range (n2):
    list2.append(int(input("Enter element:")))
    
list3 = list1 + list2

print("List 1:",list1)
print("List 2:",list2)
print("List 3:",list3)        