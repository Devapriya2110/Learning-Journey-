a=["Capuccino","Matcha","Tea","Latte","Espresso"]
b=[10,200,5000,700,900]
c=[10.23,10.23,70.6,80.95,50.32]
d=[True,False]
#DataType 
print(type(b))
#Print value in a list by index
print(a[2])
#Datatype of the value
print(type(b[0]))
#Append
b.append(100)
print(b)
#clearing a list
b.clear()
print(b)
#Copying a list 
b=c.copy()
print(b)
#Counting repetation in a list
print(c.count(10.23))
#Counting elements in a list
print(len(a))
#Concatenating Lists
print(b+c)
#Adding a value in a list
a.insert(4,"Americano")
print(a)
# Extending a list
c.extend(d)
print(c)

c.extend([10,30])
print(c)
# Finding position of a value in a list
print(a.index("Capuccino"))
# Removing a value with the help of index
a.pop(5)
print(a)
# Removing a value with the help of the value name
c.remove(30)
print(c)
# Reversing a list
d.reverse()
print(d)
# Sorting a list in ascending order
a.sort()     #in string alphabetic comparison,A<B
print(a)

b.sort()
print(b)
# Sorting a list in descending order
b.sort(reverse=True)
print(b)
#Negative indexing
print(a[-2])
print(d[-1])
#Updating a value
a[2]="Mocha"
print(a)
#Slicing
print(a[1:4])
#Memebership operator
print("Tea" in a)
print("Chai" in a)
#Looping through a list
for i in a:
    print(i)
#Looping using index
for i in range (len(a)):
    print(i,a[i])
#Deleting
del b[2]
print(b)
#Minimum
print(min(a))               #in string alphabetic comparison,A<B
print(min(b))
#Maximum
print(max(b))
#sum
print(sum(b))
#Nested list
m=[[1,2,3],
[4,5,6]]
print(m[1][2])
#List multiplication
a=[30]
print(a*5)
#List comprehension
squares=[]

for i in range (5):
    squares.append(i**2)
print(squares)

#This can also be written in a comprehensive way as:
squares=[i**2 for i in range (5)]
print(squares)


