import json

# r => load
#w => dump


f = open("demo.json","r")
data = json.load(f)
print(data)
print(type(data))