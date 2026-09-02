a=int(input("Enter marks in English:"))
b=int(input("Enter marks in Maths:"))
c=int(input("Enter marks in Science:"))
d=int(input("Enter marks in Social Studies:"))
e=int(input("Enter marks in Computer Science:"))
total_marks = 500
student_total_marks = a+b+c+d+e
p = student_total_marks/total_marks * 100
if a>100 or a<0:
    print("Marks cant be more than 100 or negative.")
elif b>100 or b<0:
    print("Marks cant be more than 100 or negative.")
elif c>100 or c<0:
    print("Marks cant be more than 100 or negative.")
elif d>100 or d<0:
    print("Marks cant be more than 100 or negative.")
elif e>100 or e<0:
    print("Marks cant be more than 100 or negative.")
else:
    print("Percentage is",p,"%")
    if p>90:
        print("Grade A")
    elif p>80:
        print("Grade B")
    elif p>70:
        print("Grade C")
    elif p>60:
        print("Grade D")
    elif(p>50):
        print("Grade E")
    else:
        print("Fail")
    