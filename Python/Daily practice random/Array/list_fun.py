a = []
# print(dir(a))
for i in dir(a):
    if "_" not in i:
        print(i)