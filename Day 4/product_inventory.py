def product():

    inventory = {}

    while True:
        print("welcome to product inventory")
        print("1. add")
        print("2. update quantity")
        print("3. product availability")
        print("4. view all details")
        print("5. quit")
        choice = input("Enter choice 1 - 5 to perform an action")

        if choice == "1":
            product_name = input("Enter product name: ")
            price = int(input(f"enter price of {product_name}: "))
            quantity = int(input(f"enter quantity of {product_name}"))
            inventory[product_name] = {"price" : price, "quantity" : quantity}

        elif choice == "2":
            product_name = input("Enter the product name to modify quantity: ")
            if product_name in inventory:
                update_qty = int(input("Enter the quantity: "))
                inventory[product_name]["quantity"] = update_qty
                print(f"quantity updated for {product_name}")
            else:
                print(f"{product_name} doesnt exist")
        
        elif choice == "3":
            product_name = input("Enter the product_name")
            if product_name in inventory:
                print(f"{product_name} exist")
                print(inventory[product_name])
            else:
                print(f"{product_name} doesnt exist")
        
        elif choice == "4":
            print("The product inventory logs are: ")
            print(inventory)

        elif choice == "5":
            print("goodbye..")
            False
        
        else:
            print("invalid choice")

product()