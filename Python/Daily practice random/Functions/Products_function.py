products = [
    {"name": "Milk", "price": 36},
    {"name": "Chocolate", "price": 20},
    {"name": "Biscuit", "price": 10},
    {"name": "Chips", "price": 40},
    {"name": "Ice cream", "price": 60}
]

def display_products():
    print("--------------------")
    print("PRODUCTS")
    for i in range(len(products)):
        print(i + 1,products[i]["name"], "~~~~~₹", products[i]["price"])
    print("--------------------")
       
def select_product():
    customer = int(input("Enter the product no.: "))

    if customer < 1 or customer > len(products):
        print("Sorry Invalid product number")
        return None

    for i in range(len(products)):
        if customer == i + 1:
            print("Yay!", products[i]["name"], "added to cart.")
            return products[i]
        
def checkout():
    while True:
        choice = input("Do you want to checkout? (Y/N): ").upper()

        if choice == "Y":
            return True

        elif choice == "N":
            print("Okay let's continue shopping")
            return False

        else:
            print("Please Enter Y or N.")
            
cart = []
            
def print_bill(cart):
    print("====================")
    print("BILL")

    total = 0

    for item in cart:
        print(item["name"], "~~~~~~ ₹", item["price"])
        total += item["price"]

    print("No.of items:", len(cart))
    print("Total price: ₹", total)
    print("Thank You for purchasing :)")
    print("====================")
    
while True:

    display_products()

    product = select_product()

    if product is None:
        continue

    cart.append(product)

    if checkout():
        break

print_bill(cart)