class Calculator:
    def v1(self,a):
        self.a = a
    
obj = Calculator()
obj2 = Calculator()

obj.v1(10)
obj2.v1(50)
print("The sum is:",obj.a + obj2.a)

obj.v1(40)
obj2.v1(60)
print("The sum is:",obj.a + obj2.a)