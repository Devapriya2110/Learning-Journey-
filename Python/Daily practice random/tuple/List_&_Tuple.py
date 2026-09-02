list = [(10,20),(30,40),(50,60)]
tuple = ([10,20],[30,40],[50,60])
a = [(10,20),(30,40),(50,60)]
b = ([10,20],[30,40],[50,60])

#List
print("List functions:")
for i in (dir(list)):
    if "_" not in i:
        print(i)
#Append
list.append((3,4))
print(list)
# clear
list.clear()
print(list)
# copy
list = a.copy()
print(list)
# extend
list.extend(a)
print(list)
# count
print(list.count((10,20)))
# index
print(list[0][0])
print(list.index((50,60)))
# insert
list.insert(3,(20,30))
print(list)
# pop
list.pop(3)
print(list)
# remove
list.remove((30,40))
print(list)
# reverse
list.reverse()
print(list)
# sort        
list.sort()
print(list)
list.sort(reverse=True)
print(list)

#Tuple
print("Tuple functions:")
for i in dir(tuple):
    if "_" not in i:
        print(i)

#Append
# tuple.append([3,4])
# print(tuple)
# clear
# tuple.clear()
# print(tuple)
# copy
# tuple = b.copy()
# print(tuple)
# extend
# tuple.extend(b)
# print(tuple)

# count
print(tuple.count([10,20]))
# index
print(tuple[0][0])
print(tuple.index([50,60]))

# insert
# tuple.insert(3,(20,30))
# print(tuple)
# pop
# tuple.pop(3)
# print(tuple)
# remove
# tuple.remove((30,40))
# print(tuple)
# reverse
# tuple.reverse()
# print(tuple)
# sort        
# tuple.sort()
# print(tuple)
# tuple.sort(reverse=True)
# print(tuple)

