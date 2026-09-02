import pickle
import json

a = {
    "ID" : "123",
    "Name":"Lucy",
    "Class" : 11,
    "Marks" : 84
}

f = open("result_pickle.pickle","wb")
pickle.dump(a,f)

f1 = open("result_pickle.pickle","rb")
pickle.load(f1)
