c=int(input("Enter a no:"))
if c%2==0 and c%11==0:
    print("This no is divisible by both 2 and 11") 
elif c%2==0 :
    print("This no is divisible by 2")
elif c%11==0:
    print("This no is divisible by 11")
else :
    print("This no is not divisible by both 2 and 11")