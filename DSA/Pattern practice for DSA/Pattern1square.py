#Simple
n = int(input("Enter no. of rows:"))
for i in range (n):
    for j in range (n):
        print("*",end=" ")
    print()
print("\n")

#With function
class Solution:
    def pattern1(self,n):
        for i in range (n):
            for j in range (n):
                print("*",end=" ")
            print()
            
sol = Solution()
sol.pattern1(5)

#My coding ninja code
def nForest(n:int) ->None:

    for i in range(n):
        for j in range(n):
            print("*",end=" ")
        print()
            
#Output
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * * 
# * * * * *
