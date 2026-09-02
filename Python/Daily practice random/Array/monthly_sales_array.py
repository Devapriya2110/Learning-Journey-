'''5.  Highest Monthly Sales Task:

-   Create an integer array with monthly sales of 10 salespersons.
-   Find the highest sales value.
-   Print the highest value and its index.'''

sales = [5000,7000,9000,10000,2500,7300,8300,9600,2000,8000]
print("Sales:",sales)

highest_sales = max(sales)
index = sales.index(highest_sales)

print("Highest sales =",highest_sales)
print("Index =",index)