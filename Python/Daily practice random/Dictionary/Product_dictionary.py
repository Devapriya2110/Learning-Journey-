products = [
    {"name" : "Milk" , "price" : 36},
    {"name" : "Chocolate", "price":20},
    {"name" : "Biscuit", "price":10},
    {"name" : "Chips", "price" :40},
    {"name" : "Ice cream", "price" : 60}
]

#Making a Cart
Cart = []
count = 0

while True:
    
    #Products display
    print("--------------------------")
    print("PRODUCTS")
    
    for i in range (len(products)):
        print(i+1,products[i]["name"],"~~~~~₹",products[i]["price"]) 
    
    print("----------------------------")
    print("\n")

    #Customer inuput 
    customer = int(input("Enter the product no.:"))
    
    if customer < 1 or customer>len(products):
        print("Sorry Invalid product number")
        continue
    
    for i in range(len(products)):
        if customer==i+1:
            print("Yay!",products[i]["name"],"added to cart.")
            Cart.append(products[i])
            count+=1
    
    #Checkout
    while True :   
        Checkout = input("Do you want to checkout?(Y/N):").upper()
        
        if Checkout == "Y":
            break
        
        elif Checkout == "N":
            print("Okay lets continue shopping")
            break
        
        else:
            print("Please Enter Y or N.")
            
    if Checkout == "Y":
        break

#Bill      
print("====================")
print("BILL")
#Price 
total = 0 
for item in Cart:
    print(item["name"], "~~~~~~ ₹", item["price"])
    total+=item["price"]   
print("No.of items:",count)
print("Total price:₹",total)
print("Thank You for purchasing :)")
print("====================")        



    

