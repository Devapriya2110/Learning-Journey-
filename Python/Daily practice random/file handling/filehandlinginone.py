import json
import pickle

a="Hello"

f1=open("fho.txt","w")
f1.write(a)
print(f1)

f=open("fho.txt","r")
f.read()
print(f)

f2=open("fho.txt","a")
b="EVERYBODY!"
f2.write(b)
print(f2)

f3 = open("fho.json","w")
c=[1,2,3]
h = json.dump(c,f3)
print(h)

f3 = open("fho.json","r")
g = json.load(f3)
print(h)
print(type(f3))