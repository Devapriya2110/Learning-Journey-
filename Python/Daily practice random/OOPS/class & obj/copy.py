class Cp:
    def v(self,a):
        self.a = a
         
    #Copy    
    def copy(self):
        self.a2 = self.a.copy()
        return self.a2
    
    #Sum
    def sum(self):
        return sum(self.a) 
    
    #Append
    def append(self,value):
        self.a.append(value)
        return self.a
        
    #Extend
    def extend(self):
        self.a.extend(self.a2)
        return self.a
    
    #Remove
    def remove(self,value):
        self.a.remove(value)
        return self.a
    
    #Insert
    def insert(self,index,value):
        self.a.insert(index,value)
        return self.a
    
    #Pop
    def pop(self,index):
        self.a.pop(index)
        return self.a
    
    #Length
    def len(self):
        return len(self.a)
    
    #Maximum
    def max(self):
        return max(self.a)
    
    #Minimum
    def min(self):
        return min(self.a)
    
    #Sort
    def sort(self):
        self.a.sort()
        return self.a
    
    #Reverse
    def rev(self):
        self.a.reverse()
        return self.a
    
    #Count
    def count(self,value):
        return self.a.count(value)
    
    #Index
    def index(self,num):
        return self.a.index(num)
    
    #Clear
    def clear(self):
        self.a2.clear()
        return self.a2
    
    #All(Checks the truthy)
    def all(self):
        return all(self.a)
    
    #Any
    def any(self):
        return any(self.a)
    
obj = Cp()

obj.v([1,2,3])
print("a:",obj.a)

#Copying
print("a2(copy of a):",obj.copy())

#Sum
print("Sum of a:",obj.sum())

#Append
print("New a:",obj.append(0))

#Extend
print("a extended by a2:",obj.extend())

#Remove
print("New a:",obj.remove(1))

#Insert
print("Updated a:",obj.insert(4,20))

#Pop
print("After removing element from indext 5 in a , Updated a:",obj.pop(5))

#Length
print("Length of a is:",obj.len())

#Maximum
print("Maximum of a:",obj.max())

#Minimum
print("Minimum of a:",obj.min())

#Sorting
print("a after sorting:",obj.sort())

#Reverse
print("Reverse of a:",obj.rev())

#Count
print("No. of 2s in a:",obj.count(2))

#Index
print("Index of 20 in a is:",obj.index(20))

#Clearing the list
print("Updated a2 after clearing:",obj.clear())

#All
print("Truthy of elements in a:",obj.all())
        
#Any
print("If any element in a is true:",obj.any())