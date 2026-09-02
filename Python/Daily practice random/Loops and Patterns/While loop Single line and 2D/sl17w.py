n = int(input("Enter a no: "))
i = 1

while i <= n:
    if i % 2 == 0:
        sign = "+"
    else:
        sign = "-"

    if i == n:
        print(sign, i, "=", end=" ")
    else:
        print(sign, i, end=" ")

    i += 1
    
#For sum
n = int(input("Enter a no: "))
i = 1
total = 0

while i <= n:
    if i % 2 == 0:
        sign = "+"
        total+=i
    else:
        sign = "-"
        total-=i

    if i == n:
        print(sign, i, "=", end=" ")
    else:
        print(sign, i, end=" ")

    i += 1
print(total)