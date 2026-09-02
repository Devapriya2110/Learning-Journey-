import json
import pickle

#Pickle file read
file = open("users.pickle", "rb")
users = pickle.load(file)
file.close()


file = open("products.json","r")     # We can also use:# with open("products.json", "r") as file:                                    #   data = json.load(file)
products = json.load(file)
file.close()

#Register & Login

logged_in = False
while not logged_in:    
    print("------------------------")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("------------------------")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        username = input("Enter username: ")
        password = input("Enter password: ")

        user = {
            "username": username,
            "password": password
        }

        users.append(user)
        
        file = open("users.pickle","wb")
        pickle.dump(users,file)
        file.close()
        
        print("Registration Successfull!")
        
    elif choice == 2:
        username = input("Enter username: ")
        password = input("Enter password: ")

        found = False 
        
        for user in users:
            if user["username"] == username and user["password"]  == password:
                found = True
                break
            
        if found:
            print("Login successful!")
            logged_in = True
        else:
            print("Incorrect username or password")
            
    elif choice == 3:
        print("BYEEEEE")
        break
    
    else:
        print("Invalid Choice")
            
if logged_in:                   
    categories = list(products.keys())

    cart = []  

    while True:
        i=1
        #Displaying Categories
        print("++++++++++++++++++++++++++++++")
        print("          CATEGORY          ")
        for category in products.keys():
        
            print(i,".",category)
            i+=1
        print("++++++++++++++++++++++++++++++")

        choice = int(input("Enter your choice:"))
            
        category = categories[choice-1]

        subcategories = list(products[category].keys())
        j = 1

        #Displaying Subcategory
        print("++++++++++++++++++++++++++++++")
        print("          SUBCATEGORY         ")
        for subcategory in products[category].keys():
            print(j,".",subcategory)
            j+=1
        print("++++++++++++++++++++++++++++++")

        choose = int(input("Enter your choice:"))
        subcategory = subcategories[choose-1]

        products_list = products[category][subcategory]
        k=1

        print("++++++++++++++++++++++++++++++")
        print("           PRODUCTS           ")
        #Displaying products
        for product in products_list:
            print("ID:",product["id"])
            print("Name:",product["name"])
            print("Color:",product["color"])
            print("Price:",product["price"])
            print("Stock:",product["stock"])
            print("\n")
            k+=1
        print("++++++++++++++++++++++++++++++")

        product_id = int(input("Enter product ID:"))
        quantity = int(input("Enter How many of the product you want:"))
                
        #Getting products that could be added to cart
        found = False

        for product in products_list:
            if product_id == product["id"]:
                found =  True
                selected_product = product
                break
            
        if not found:
            print("Product not found!Enter valid product ")
            continue
        
        #Cart  - ADD PRODUCT
        cart_found = False
        for item in cart:
            if product_id == item["id"]:
                cart_found = True
                
                if quantity <= selected_product["stock"]:
                    item["qty"] += quantity
                    selected_product["stock"] -= quantity
                    print("Quantity updated")
                else:
                    print("Not enough stock")
                    
                break
                    
        if not cart_found:
            if quantity <= selected_product["stock"]:
                    cart_item = {
                            "id":selected_product["id"],
                            "name":selected_product["name"],
                            "color":selected_product["color"],
                            "price":selected_product["price"],
                            "qty":quantity
                    }
                    
                    cart.append(cart_item)
                    selected_product["stock"] -= quantity
                    
                    print("Item added to cart")
            else:
                print("Not enough Stock")
                
        #CART Actions
        checkout = False
        
        while True:
            print("++++++++++++++++++++++++++++++")
            print("          CART MENU")
            print("1. Add another product")
            print("2. Remove from cart")
            print("3. View cart")
            print("4. Checkout")
            print("5. Exit")
            print("++++++++++++++++++++++++++++++")
            
            cart_choice = int(input("Enter your choice:"))
            
            #Add another product
            if cart_choice == 1:
                break
            
            #Remove product
            elif cart_choice == 2:
                
                if len(cart) == 0:
                    print("Cart is Empty")
                    continue
                
                remove_id = int(input("Enter product ID to remove: "))

                remove_found = False
                
                for item in cart :
                    
                    if remove_id == item["id"]:
                        remove_found = True
                        
                        #Return stock
                        for product in products_list:
                            if remove_id == product["id"]:
                                product["stock"] += item["qty"]
                                break
                            
                        cart.remove(item)
                        print("Item removed from cart")
                        break
                    
                if not remove_found:
                    print("Product not found in cart")
            
            #View cart          
            elif cart_choice == 3:
                print("++++++++++++++++++++++++++++++")
                print("             CART             ")
                print("++++++++++++++++++++++++++++++")
                
                if len(cart) == 0:
                    print ("Cart is empty")
                else:
                    total = 0
                    
                    for item in cart:
                        print("ID:",item["id"])
                        print("Name:",item["name"])
                        print("Color:",item["color"])
                        print("Price:",item["price"])
                        print("Quantity:",item["qty"])
                        
                        #Price in car
                        item_total = item["price"] * item["qty"]
                        print("Item Total:",item_total)
                        print("\n")
                        print("----------------------------------")
                        
                        total+=item_total
                        
                    print("Grand total:",total)
                    print("++++++++++++++++++++++++++++++")
            
            #Checkout
            elif cart_choice == 4:
                if len(cart) == 0:
                    print("Cart is empty")
                else:
                    checkout = True 
                    break
                
            elif cart_choice == 5:
                print("Bye")
                break 
            
            else:
                print("Invalid input ")

        #Checkout indetail
        if checkout :
            print("++++++++++++++++++++++++++++++")
            print("          CHECKOUT")
            print("++++++++++++++++++++++++++++++")
            
            total = 0
            
            for item in cart:
                item_total = item["price"] * item["qty"]
                total += item_total

                print("Name:", item["name"])
                print("Price:", item["price"])
                print("Quantity:", item["qty"])
                print("Item Total:", item_total)
                print("------------------------------")
                
            print("Grand Total:", total)
            
            confirm = input("Proceed to checkout? (Y/N): ").upper()
            
            if confirm == "N":
                checkout = False
                continue
            
            elif confirm == "Y":
                print("Payment Succesful!")
                
            else:
                print("Invalid input")
                
            #Bill
            print("++++++++++++++++++++++++++++++")
            print("             BILL")
            print("++++++++++++++++++++++++++++++")

            total = 0
            
            for item in cart:
                item_total = item["price"] * item["qty"]

                print("ID:", item["id"])
                print("Name:", item["name"])
                print("Price:", item["price"])
                print("Quantity:", item["qty"])
                print("Item Total:", item_total)
                print("------------------------------")

                total += item_total

            print("Grand Total:", total)
            print("++++++++++++++++++++++++++++++")
            print("       Thank you for shopping!")
            
            file = open("products.json","w")
            json.dump(products,file,indent=4)
            file.close()
            break
        
                    
            

            
        
        
        