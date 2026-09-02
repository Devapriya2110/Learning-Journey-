Colors = {"Red","Green","Blue","Yellow","Pink","Purple","White","Brown"}
cl = {"Red","Green","Blue","Yellow","Pink","Purple"}
cl2 = {"Red","Green","Blue","Yellow","Pink","Purple","White","Brown"}        
for i in dir(Colors):
    if "_" not in i:
        print(i)

print("Set functions:")
#add
Colors.add("Black")
print(Colors)
# clear
Colors.clear()
print(Colors)
# copy
Colors = cl2.copy()
print(Colors)
# difference
print(cl2.difference(cl))
# discard
print(Colors)
Colors.discard("White")
print(Colors)
# intersection
print(Colors.intersection(cl))
# isdisjoint
print(Colors.isdisjoint(cl))
# issubset
print(cl.issubset(Colors))
# issuperset
print(Colors.issuperset(cl))
# pop
Colors.pop()
print(Colors)
# remove
Colors.remove("Yellow")
print(Colors)
# union
Colors.union(cl)
print(Colors)
# update
Colors.update(cl)
print(Colors)
#type
print(type(Colors))