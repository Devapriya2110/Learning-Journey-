def add(a,b):
    return a+b

def sub(a,b):
    return a-b
    
def mul(a,b):
    return a*b
    
def div(a,b):
    return a/b
    
def rem(a,b):
    return a%b
    
while True:       
    print("--------------------")
    print("ARITHMETIC OPERATIONS")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")
    print("5.Remainder")
    print("0.End")
    print("--------------------")
    
    a = int(input("Enter a no:"))
    b = int(input("Enter another no:"))
    
    user = int(input("Enter the operation you would like to perform:"))
    
    if user == 1:
        print("Addition:",add()) 
    
    elif user == 2:
        sub("Subtraction:",sub()) 
        
    elif user == 3:
        mul()
    
    elif user == 4:
        div()
    
    elif user == 5:
        rem()
        
    elif user == 0:
        print("END")
        break
    else:
        print("Invalid input!")  
        
      


        