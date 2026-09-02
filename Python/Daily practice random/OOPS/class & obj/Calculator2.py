class Calculator:
    def value(self,a):
        self.a = a
    def value2(self,b):
        self.b = b
        
    def add(self):
        return self.a + self.b

    def sub(self):
        return self.a - self.b
        
    def mul(self):
        return self.a * self.b
        
    def div(self):
        return self.a / self.b
        
    def rem(self):
        return self.a % self.b
        
obj1 = Calculator()

while True:
    a = int(input("Enter a no:"))
    b = int(input("Enter a no:"))

    obj1.value(a)
    obj1.value2(b)

    print("-------------------------------")
    print("          Calculator           ")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Remainder")
    print("6.Exit")
    print("-------------------------------")

    c = int(input("Enter which operation you want to perform:"))

    if c == 1:
        print("Addition:",obj1.add())
         
    elif c==2:  
        print("Subtraction:",obj1.sub())
           
    elif c==3:
        print("Multiplication:",obj1.mul())
        
    elif c==4:
        print("Division:",obj1.div())
        
    elif c==5:
        print("Remainder:",obj1.rem())
        
    elif c==6:
        print("BYEEEEEE!")
        break    
    else:
        print("Not a valid Input!Pls enter proper operation you want to perform.")
        




