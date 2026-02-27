def shop_list():

    print("Welcome to shop list managment portal")
    print("please press one of the keys to access the portal")
    shop = input("'A' to add items, 'V' to view list, 'Q' to quit: ")

    

    while shop !="q" or shop !="Q":

        new_list = ["apple", "banana", "orange", "watermelon", "kiwi"]
        if shop == "V" or shop =="v":
            print(new_list)
            break
        elif shop == "A" or shop =="a":
            j = str(input("Enter the value you want to add to the list: "))
            appended_list = new_list.append(j)
            print(f"the updated list is {new_list}")
            break
        elif shop == "R" or shop =="r":
            i = str(input("Enter the value you want to delete: "))
            remove_element = new_list.remove(i)
            print(new_list)
            break
        elif shop == "q" or shop == "Q":
            break
        else:
            print("invalid key, press a valid key")
            break

shop_list()