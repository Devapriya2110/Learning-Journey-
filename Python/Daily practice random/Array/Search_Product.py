'''2.  Search Product ID Task:
-   Create an integer array with 10 product IDs.
-   Accept a product ID from the user.
-   Search the array.
-   Print the index if found; otherwise print “Product Not Found.”'''
product = []

for i in range (10):
    product.append(int(input("Enter Product ID:")))
    
print("Product IDs:",product)
    
search = int(input("Enter Product ID to search:"))

for i in range (len(product)):
    if search == product[i]:
        print("Product is at index:",i)
        break
else:
    print("Product not found")
        