import json
email = input("Enter email : ")
password = input("Enter password : ")

user = {
    "email": email,
    "passwoord":password
}
f1 = open("demo.json","r")
users = json.load(f1)
print(users)

users.append(user)



f2 = open("demo.json","w")
json.dump(users,f2)