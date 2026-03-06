import csv
import os
def product():

    filename = "Week 2/Day 1/Products.csv"

    try:
        product = []

        
        with open(filename, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                product.append(row)
    
    except Exception as e:
        print(f"File not found: {e}")

    under_50 = list(filter(lambda x:float(x['Price'])>50, product))
    rating = list(filter(lambda x:float(x['Rating'])>4.0, product))
    category = list(filter(lambda x:x['Category'] == "Footwear", product))
    asc = sorted(product, key = lambda x : float(x['Price']) )
    desc = sorted(product, key = lambda x:float(x['Rating']), reverse = True)
    asc_alpha = sorted(product, key = lambda x:x['Product '])
    multi = sorted(product, key = lambda x: (x['Category'], float(x['Price'])))

    text = "Week 2/Day 1/product.txt"

    try:
    
        reports = f"""PRODUCT DATA
    
All Products: {product}
Products under $50: {under_50}
Rating above 4.0: {rating}
Footwear: {category}
Sorted based on price: {asc}
Reverse sorted based on rating: {desc}
Sorted based on Alphabet: {asc_alpha}
Sorted based on Category and Price: {multi}

"""
        if not os.path.exists(text):
            with open(text, "w") as file:
                file.write(reports)
    
    except Exception as e:
        print(f"File not created: {e}")


product()