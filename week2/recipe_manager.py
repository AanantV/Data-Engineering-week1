import os
import json
import csv

def recipe_manager():
    path = "Week 2/Day 2/"
    if not os.path.exists(path):
        os.makedirs(path)

    fn = os.path.join(path, "recipe.json")
    filename = os.path.join(path, "recipe.csv")
    fields = ['Name', 'Category', 'Ingredients', 'Instruction']

    def initialise(filename):
        try:
            if not os.path.exists(filename):
                with open(filename, "w", newline='') as file:
                    writer = csv.DictWriter(file, fieldnames=fields)
                    writer.writeheader()
        except Exception as e:
            print(f"File not created: {e}")

    def add_recipe():
        ingredients = []
        name = input("Enter the recipe name: ")
        category = input("Enter the category: ")
        try:
            count = int(input("How many ingredients you want to add? "))
        except ValueError:
            print("Invalid number. Setting count to 0.")
            count = 0

        for i in range(count):
            i_name = input(f"Ingredient {i+1} name: ")
            i_quantity = input("Quantity: ")
            i_unit = input("Unit: ")
            ingredients.append({"name": i_name, "quantity": i_quantity, "unit": i_unit})

        instructions = input("Enter the instruction for the recipe: ")

        ingredients_string = ", ".join([f"{ing['quantity']} {ing['unit']} {ing['name']}" for ing in ingredients])

        with open(filename, "a", newline='') as file:
            writer = csv.DictWriter(file, fieldnames=fields)
            writer.writerow({
                'Name': name, 
                'Category': category, 
                'Ingredients': ingredients_string, 
                'Instruction': instructions
            })

        try:
            recipes = []
            if os.path.exists(fn) and os.path.getsize(fn) > 0:
                with open(fn, "r") as file:
                    recipes = json.load(file)

            recipe_data = {
                "name": name,
                "category": category,
                "ingredients": ingredients, 
                "instruction": instructions
            }

            recipes.append(recipe_data)

            with open(fn, "w") as json_file:
                json.dump(recipes, json_file, indent=4)

            print(f"Success! '{name}' added.")
        except Exception as e:
            print(f"JSON error: {e}")

    def view_recipe():
        try:
            search_name = input("Enter the name of the recipe: ").lower()
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    if row['name'].lower() == search_name:
                        print(f"\nRecipe Name: {row['name']}")
                        print(f"Category: {row['category']}")
                        print(f"Instructions: {row['instruction']}")
        except Exception as e:
            print(f"Error viewing recipe: {e}")

    def ingredient_search():
        try:
            ing_name = input("Enter the ingredient: ").lower()
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    for ing in row['ingredients']:
                        if ing_name in ing['name'].lower():
                            print(f"- {row['name']} (Category: {row['category']})")
                            break
        except Exception as e:
            print(f"JSON error: {e}")

    def category_search():
        try:
            c_name = input("Enter the category: ").lower()
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    if c_name == row['category'].lower():
                        print(f"- {row['name']}")
        except Exception as e:
            print(f"JSON error: {e}")

    def shopping_list():
        try:
            dish = input("Enter the dish name: ").lower()
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    if dish in row['name'].lower():
                        print(f"\nShopping List for {row['name']}:")
                        for item in row['ingredients']:
                            print(f"[] {item['quantity']} {item['unit']} {item['name']}")
        except Exception as e:
            print(f"JSON error: {e}")

    initialise(filename)

    while True:
        print("\n--- RECIPE MANAGER ---")
        print("1. Add Recipe")
        print("2. View Specific Recipe")
        print("3. Search by Ingredient")
        print("4. Search by Category")
        print("5. Shopping List")
        print("6. Quit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_recipe()
        elif choice == "2":
            view_recipe()
        elif choice == "3":
            ingredient_search()
        elif choice == "4":
            category_search()
        elif choice == "5":
            shopping_list()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

recipe_manager()