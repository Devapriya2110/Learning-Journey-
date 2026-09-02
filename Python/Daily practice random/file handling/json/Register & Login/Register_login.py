import json

while True:
    print("*******************************")
    print("1.Register")      
    print("2.Login")      
    print("3.Exit")      
    print("*******************************")
    try:
        user_choice = int(input("Enter the operation no. you want to perform:"))
    except ValueError:
        print("Please enter a number!")
        continue

    if user_choice == 1:
        email = input("Enter email:")
        password = input("Enter password:")
        f = open("register.json","w")
        # a =  open("")      
    

