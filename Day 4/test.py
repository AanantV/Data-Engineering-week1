def test():

    person ={"name" : "aanant", "city" : "Chennai", "hobby" : "drawing"}
    print(person["name"])
    print(person["city"])
    print(person["hobby"])

    person["age"] = 24
    person["hobby"] = "dancing"

    print(person)

    products = {"apple" : 1.50, "banana":0.80, "orange":2.00, "milk":3.50, "bread":2.50}

    highest_price = 0
    most_expensive =''

    for key,value in products.items():
        #print(key,value)
        if value > highest_price:
            highest_price = value
            most_expensive = key
            print(f"The highest pricy product is {most_expensive}: {highest_price}")

    person = {"name" : "Sarah", "hobbies": ["reading", "gaming" , "cooking"]}

    print(person["hobbies"])
    person["hobbies"].append("dancing")
    print(person["hobbies"])

    print(len(person["hobbies"]))

    for hobby in person["hobbies"]:
        print(hobby)

    contacts = {
        "john" :{
            "phone" : 9080765,
            "email" : "johnpork@email.com"
        },
        "Sarah" :{
            "phone" : 90987765,
            "email" : "Sarah@email.com"
        }
    }

    print(contacts["john"]["phone"])

    contacts["mike"] = {
        "phone" : 2637382,
        "email" : "mike@gmail.com"
    }

    contacts["Sarah"]["phone"] = 876392

    for key,value in contacts.items():
        print(key, value["email"])


   # print(contacts)



test()