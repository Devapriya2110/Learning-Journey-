print("-----Calculator-----")
while True:
    
    #First no.
    while True:
        a = input("Enter first no:").strip()
        
        check = a
        
        if check == "":
            print("Invalid input! Enter a number.")
            continue
        
        if check[0] == "-":
            check = check[1:]
            
        if check.count(".")>1:
            print("Invalid number.")
            continue
            
        check=check.replace(".","",1)
        
        if check.isdigit():
            a=float(a)
            break
        else:
            print("Please enter a valid number.")
            
    #Operator
    while True:
        op = input("Enter operator (+ - * / %):").strip()
        
        if op in ["+","-","*","/","%"]:
            break
        else:
            print("Invalid operator.")
            
    #Second no.
    while True:
        b = input("Enter second no:").strip()
        
        check=b
        
        if check == "":
            print("Input cannot be empty.")
            continue
            
        if check[0] ==  "-":
            check=check[1:]
            
        if check.count(".")>1:
            print("Invalid number.")
            continue
            
        check = check.replace(".","",1)
        
        if check.isdigit():
            b=float(b)
            break
        else:
            print("Please enter valid number.")
            
    #Calculations
    
    if op == "+":
        print("Answer =", a + b)

    elif op == "-":
        print("Answer =", a - b)

    elif op == "*":
        print("Answer =", a * b)

    elif op == "/":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print("Answer =", a / b)

    elif op == "%":
        if b == 0:
            print("Cannot divide by zero.")
        else:
            print("Answer =", a % b)
   
    #Continue
    
    while True:
        
        choice = input("Do you want to continue the calculation?(Y/N):").upper()
        
        if choice == "Y":
            break
            
        elif choice == "N":
            print("Okay!")
            exit()
            
        else:
            print("Please enter only Y or N.")
            
            


