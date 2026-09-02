Products = [
    {
        "Milk": [
            {
                "Company_name": "Amul",
                "Products": [
                    {"Type": "Amul Gold", "Price": 35, "Quantity": "500 ml"},
                    {"Type": "Amul Shakti", "Price": 36, "Quantity": "1 L"},
                    {"Type": "Amul Taaza", "Price": 28, "Quantity": "200 ml"}
                ]
            },
            {
                "Company_name": "Sumul",
                "Products": [
                    {"Type": "Sumul Cow Milk", "Price": 30, "Quantity": "500 ml"},
                    {"Type": "Sumul Shakti", "Price": 50, "Quantity": "1 L"},
                    {"Type": "Sumul Taaza", "Price": 60, "Quantity": "1 L"}
                ]
            }
        ]
    },

    {
        "Icecream": [
            {
                "Company_name": "Vadilal",
                "Products": [
                    {"Type": "Cup", "Flavour": "Strawberry", "Price": 15, "Quantity": "50 g"},
                    {"Type": "Cup", "Flavour": "Vanilla", "Price": 25, "Quantity": "100 g"},
                    {"Type": "Cone", "Flavour": "Chocolate", "Price": 170, "Quantity": "150 g"},
                    {"Type": "Tub", "Flavour": "Butterscotch", "Price": 450, "Quantity": "300 g"},
                    {"Type": "Cup", "Flavour": "Mango", "Price": 170, "Quantity": "500 g"}
                ]
            },

            {
                "Company_name": "Kwality Wall's",
                "Products": [
                    {"Type": "Cone", "Flavour": "Cadbury Crackle", "Price": 30, "Quantity": "70 g"},
                    {"Type": "Tub", "Flavour": "Oreo & Cream", "Price": 70, "Quantity": "105 g"},
                    {"Type": "Stick", "Flavour": "Vanilla Supreme", "Price": 100, "Quantity": "120 g"},
                    {"Type": "Cup", "Flavour": "Kesar Pista", "Price": 180, "Quantity": "90 g"},
                    {"Type": "Cup", "Flavour": "Caramel Pop", "Price": 300, "Quantity": "700 g"}
                ]
            }
        ]
    },

    {
        "Chips": [
            {
                "Company_name": "Balaji",
                "Products": [
                    {"Type": "Flat Cut Wafers", "Flavour": "Simply Salted", "Price": 10, "Quantity": "35 g"},
                    {"Type": "Crunchex", "Flavour": "Masala Masti", "Price": 20, "Quantity": "65 g"},
                    {"Type": "Chataka Pataka", "Flavour": "Tomato Twist", "Price": 35, "Quantity": "80 g"},
                    {"Type": "Crunchex", "Flavour": "Cream & Onion", "Price": 40, "Quantity": "140 g"}
                ]
            },

            {
                "Company_name": "Lays",
                "Products": [
                    {"Type": "Classic Flat Cut", "Flavour": "Classic Salted", "Price": 10, "Quantity": "23 g"},
                    {"Type": "Lays Maxx", "Flavour": "Indian Magic Masala", "Price": 20, "Quantity": "58 g"},
                    {"Type": "Lays Wafer Style", "Flavour": "Hot n Sweet Chilli", "Price": 35, "Quantity": "80 g"},
                    {"Type": "Classic Flat Cut", "Flavour": "Spanish Tomato", "Price": 38, "Quantity": "143 g"}
                ]
            }
        ]
    }
]


Cart = []


# -------------------------------
# DISPLAY CATEGORIES
# -------------------------------

def display_categories():

    print("\n==============================")
    print("         CATEGORIES")
    print("==============================")

    for i in range(len(Products)):

        for category in Products[i]:

            print(i + 1, ".", category)


# -------------------------------
# DISPLAY PRODUCTS OF CATEGORY
# -------------------------------

def display_category(category):

    print("\n==============================")
    print("          PRODUCTS")
    print("==============================")

    number = 1

    for category_name in category:

        print("\nCategory:", category_name)
        print("------------------------------")

        companies = category[category_name]

        for company in companies:

            print("\nCompany:", company["Company_name"])

            for product in company["Products"]:

                print(
                    number,
                    ".",
                    product["Type"],
                    product.get("Flavour", ""),
                    "- ₹", product["Price"],
                    "-", product["Quantity"]
                )

                number = number + 1


# -------------------------------
# GET PRODUCTS FROM CATEGORY
# -------------------------------

def get_category_products(category):

    category_products = []

    for category_name in category:

        companies = category[category_name]

        for company in companies:

            for product in company["Products"]:

                product_copy = product.copy()

                product_copy["Company"] = company["Company_name"]
                product_copy["Category"] = category_name

                category_products.append(product_copy)

    return category_products


# -------------------------------
# ADD TO CART
# -------------------------------

def add_to_cart():

    display_categories()

    choice = input("\nChoose category (B to go back): ")

    if choice.upper() == "B":
        return

    if not choice.isdigit():

        print("Please enter a valid number.")
        return

    choice = int(choice)

    if choice < 1 or choice > len(Products):

        print("Invalid category!")
        return

    category = Products[choice - 1]

    display_category(category)

    category_products = get_category_products(category)

    product_choice = input(
        "\nChoose product (B to go back): "
    )

    if product_choice.upper() == "B":
        return

    if not product_choice.isdigit():

        print("Please enter a valid number.")
        return

    product_choice = int(product_choice)

    if product_choice < 1 or product_choice > len(category_products):

        print("Invalid product!")
        return

    product = category_products[product_choice - 1]

    quantity = input("Enter quantity: ")

    if not quantity.isdigit():

        print("Please enter a valid quantity.")
        return

    quantity = int(quantity)

    if quantity <= 0:

        print("Quantity must be greater than 0.")
        return

    Cart.append({
        "Category": product["Category"],
        "Company": product["Company"],
        "Type": product["Type"],
        "Flavour": product.get("Flavour", ""),
        "Price": product["Price"],
        "Quantity": quantity,
        "Size": product["Quantity"]
    })

    print("\nProduct added to cart!")


# -------------------------------
# DISPLAY CART
# -------------------------------

def display_cart():

    if len(Cart) == 0:

        print("\nCart is empty!")
        return

    print("\n==============================")
    print("            CART")
    print("==============================")

    total = 0

    for i in range(len(Cart)):

        item = Cart[i]

        amount = item["Price"] * item["Quantity"]

        print("\nItem", i + 1)
        print("Category :", item["Category"])
        print("Company  :", item["Company"])
        print("Product  :", item["Type"])

        if item["Flavour"] != "":
            print("Flavour  :", item["Flavour"])

        print("Price    : ₹", item["Price"])
        print("Quantity :", item["Quantity"])
        print("Size     :", item["Size"])
        print("Amount   : ₹", amount)

        total = total + amount

    print("\n------------------------------")
    print("TOTAL = ₹", total)


# -------------------------------
# CHECKOUT
# -------------------------------

def checkout():

    if len(Cart) == 0:

        print("\nCart is empty!")
        return False

    print("\n==============================")
    print("             BILL")
    print("==============================")

    total = 0

    for i in range(len(Cart)):

        item = Cart[i]

        amount = item["Price"] * item["Quantity"]

        print(
            i + 1,
            ".",
            item["Company"],
            item["Type"],
            item["Flavour"],
            "x", item["Quantity"],
            "= ₹", amount
        )

        total = total + amount

    print("------------------------------")
    print("TOTAL = ₹", total)
    print("==============================")

    print("Thank you for shopping!")

    return True


# -------------------------------
# MAIN PROGRAM
# -------------------------------

while True:

    print("\n==============================")
    print("       SHOPPING SYSTEM")
    print("==============================")

    print("1. Add Product")
    print("2. View Cart")
    print("3. Checkout")
    print("4. Exit")

    choice = input("\nEnter choice: ")

    if choice == "1":

        add_to_cart()

    elif choice == "2":

        display_cart()

    elif choice == "3":

        if checkout():
            break

    elif choice == "4":

        print("\nThank you!")
        break

    else:

        print("\nInvalid choice!")