class Test:
    def get_value(self,a):    
        self.a = a
    
    def display(self):
        print(f"the value of a  = {self.a}")

obj = Test()

obj.get_value(10)
obj.display()
print(obj.a)



