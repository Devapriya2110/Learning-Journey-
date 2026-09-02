class Calculator:
    def get_value(self,a):
        self.a = a

obj1 = Calculator()
obj2 = Calculator()

a = int(input("Enter a no:"))
b = int(input("Enter a no:"))

obj1.get_value(a)
obj2.get_value(b)

print("-------------------------------")
print("          Calculator           ")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Remainder")
print("6.Exit")
print("-------------------------------")

while True:
    c = int(input("Enter which operation you want to perform:"))

    if c == 1:
        print("Addition:",obj1.a + obj2.a)
        continue    
    elif c==2:  
        print("Subtraction:",obj1.a - obj2.a)
        continue    
    elif c==3:
        print("Multiplication:",obj1.a * obj2.a)
        continue
    elif c==4:
        print("Division:",obj1.a / obj2.a)
        continue
        
    elif c==5:
        print("Remainder:",obj1.a % obj2.a)
        continue
    elif c==6:
        print("BYEEEEEE!")
        break    
    else:
        print("Not a valid Input!Pls enter proper operation you want to perform.")
        continue


