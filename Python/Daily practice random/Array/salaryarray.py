'''3.  Update Employee Salary Task:

-   Create an integer array with 10 employee salaries.
-   Ask the user for the old salary and the new salary.
-   Update the matching salary.
-   Print the updated array.'''

salary = [25000,80000,50000,30000,20000,35000,45000,55000,60000,15000]

print("Original salary:",salary)  
 
oldsalary = int(input("Enter old salary:"))
newsalary = int(input("Enter new salary:"))

found = False

for i in range(len(salary)):
    if salary[i] == oldsalary:
        salary[i] = newsalary
        found=True
        
if found:
    print("Updated Salary:", salary)
else:
    print("Salary not found")
