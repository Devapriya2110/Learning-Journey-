import pickle

#wb - write binary
#rb - read binary

a = [1,2,3,4,4,5,6,4,3,2]
f2 = open("demo.pickle","wb")
pickle.dump(a,f2)

f1 = open("demo.pickle","rb")
users = pickle.load(f1)
print(users)
