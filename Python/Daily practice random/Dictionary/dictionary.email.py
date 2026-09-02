User_data = [{"email" : "abc@gmail.com",
              "password" : "abc@123"},
             {"email" : "def@gmail.com",
              "password" : "def@456"},
             {"email" : "ghi@gmail.com",
              "password" : "ghi@789"}
            ]

email = input("Enter Email:")
password = input("Enter Password:")

Login = {"email" : email ,"password" : password}
print(Login)

found = False 

for i in User_data:
    if Login["email"] == i["email"]:
        found = True
        
        if Login["password"] == i["password"]:
            print("Login Successful!")
        else:
            print("Invalid Password")
        break
            
if found == False:
    print("User not found.")
            