import json

# r => load
#w => dump

# a = [1,2,3,34,4,5,6,34]
a = {"name":"raj","email":"raj@gmail.com"}
f = open("demo.json","w")
json.dump(a,f)