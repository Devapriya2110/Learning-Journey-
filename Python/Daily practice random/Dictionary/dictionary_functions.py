a = {"email" : "shinchan@gmail.com" ,"password" : "shinchan@123"}
b = {"email" : "shinchan@gmail.com" ,"password" : "shinchan@123"}

for i in dir(a):
    if '_' not in i:
        print(i)
 
# clear
a.clear()
print(a)
# copy
a = b.copy()
print(a)
# fromkeys
k = dict.fromkeys(a)
print(k)
# get
print(a.get("password"))
# items
for key,value in a.items():
    print(key,"=",value)
# keys
for key in a.keys():
    print(key)
# pop
b.pop("password")
print(b)
# popitem
b.popitem()
print(b)
# setdefault
a.setdefault("name","Shinchan")
print(a)
# update
a.update({"email":"nohara@gmail.com"})
print(a)
# values  
for value in a.values():
    print(value)
 



        
        
