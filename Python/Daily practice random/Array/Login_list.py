user_data = [
            ["user1@gmail.com","user@123"],
            ["user2@gmail.com","user@456"],
            ["user3@gmail.com","user@789"],
            ["user4@gmail.com","user@312"],
            ["user5@gmail.com","user@654"]]
            
email=input("Enter the email : ")
password=input("Enter the password : ")
login_data = [email,password]

f = 0
for i in user_data:
    if i[0] == login_data[0]:
        if i[1] == login_data[1]:
            print("login .. !")
            f=1
            break
        f=2
            
if f==0:
    print("user not found...!")
    
elif f==2:
    print("password does not match..!")


    
    
    
    
    
    