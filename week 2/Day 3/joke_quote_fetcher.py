import os
import json
from datetime import datetime
import requests

def joke():

    Jokes = "https://official-joke-api.appspot.com/random_joke"
    multiple_joke = "https://official-joke-api.appspot.com/jokes/random"
    Quotes = "https://dummyjson.com/quotes/random"

    joke_file = "Week 2/Day 3/Joke_Quote/jokes.json"
    joke_multi = "Week 2/Day 3/Joke_Quote/multiple_jokes.json"
    quote_file = "Week 2/Day 3/Joke_Quote/quotes.json"
    fav_file = "Week 2/Day 3/Joke_Quote/fav.json"

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")


    def get_random_joke():

        try:
            joke_list = []
            response1 = requests.get(Jokes)

            with open(joke_file, "r") as file:
                joke_list = json.load(file)

            if response1.status_code == 200:
                joke_json = response1.json()

                print(f"Setup: {joke_json['setup']}")
                print(f"Punchline: {joke_json['punchline']}")

            jokes = {
                "ID" : joke_json['id'],
                "Setup": joke_json['setup'],
                "Punchline": joke_json['punchline'],
                "Type": joke_json['type']
            }

            joke_list.append(jokes)

            with open(joke_file, "w") as file:
                json.dump(joke_list,file, indent = 4)

            print(f"Joke saved on {joke_file}")

        except Exception as e:
            print(f"Punchline failed you clown: {e}")

    def display_joke():

        try:
            if os.path.exists(joke_file):
                with open(joke_file,"r") as file:
                    reader = json.load(file)
                for row in reader:
                    input("Press enter to load the setup")
                    print(f"Setup: {row['Setup']}")
                    input("...Press enter to reveal the punchline")
                    print(f"Puncline: {row['Punchline']}")    
                
        except Exception as e:
            print(f"Punchline failed you clown: {e}")

    def get_multiple_jokes():

        try:
            multi = []
            count = int(input("Enter the number of jokes you want to generate? "))

            parameter = {
                "result": count
            }

            # if os.path.exists(joke_multi) and os.path.getsize(joke_multi) > 0:
            #     with open(joke_multi, "r") as file:
            #         multi = json.load(file)
            # else:
            #     multi = []
                
            for _ in range(count):
                response1 = requests.get(multiple_joke,params = parameter)
                content = response1.json()
                data = {
                "Type": content.get('type'),
                "Setup": content.get('setup'),
                "Punchline": content.get('punchline'),
                "ID": content.get('id')
                }
                multi.append(data)

            with open(joke_multi, "w") as file:
                json.dump(multi,file,indent=4)

            print("Data loaded successfully")

            for row in multi:
                input("Press enter for setup")
                print(f"Setup: {row['Setup']}")
                input("Press Enter for punchline")
                print(f"Punchline: {row['Punchline']}")

        except Exception as e:
            print(f"Error found: {e}")

    def quote_fetcher():
        try:
            quote_list = []
            if not os.path.exists(quote_file):
                with open(quote_file,"w") as file:
                    json.dump([],file)

            if os.path.exists(quote_file) and os.path.getsize(quote_file)>0:
                with open(quote_file,"r") as file:
                    quote_list = json.load(file)

            response2 = requests.get(Quotes)
            if response2.status_code ==200:
                data = response2.json()
                print(f"Quote: {data['quote']}")
                print(f"Author: {data['author']}")

                q = {
                    "ID": data['id'],
                    "Quote": data['quote'],
                    "Author": data['author']
                }

                quote_list.append(q) 

            with open(quote_file,"w") as file:
                json.dump(quote_list,file,indent=4)

        except Exception as e:
            print(f"Error Found: {e}")

    def display_quote():

        try:
            if os.path.exists(quote_file):
                with open(quote_file,"r") as file:
                    reader = json.load(file)
                for row in reader:
                    input("Press enter to load the Quote")
                    print(f"Quote: {row['Quote']}")
                    input("...Press enter to reveal the Author")
                    print(f"Author: {row['Author']}")    
                
        except Exception as e:
            print(f"Error: {e}")

    def save_favourite():
        try:
            fav_list=[]
            while True:
                print("Enter the type of item you want to get")
                i = input("For joke, Enter 'J' for quote, Enter 'Q' and for exit, Enter 'e': ")

                if not os.path.exists(fav_file):
                    with open(fav_file,"w") as file:
                        json.dump([],file)

                if os.path.exists(fav_file) and os.path.getsize(fav_file)>0:
                    with open(fav_file,"r") as file:
                        fav_list = json.load(file)

                if i == "J" or i=="j":
                    while True:
                        response1 = requests.get(Jokes)
                        content = response1.json()
                        if response1.status_code == 200:
                            print(f"Setup: {content['setup']}")
                            print(f"Punchline: {content['punchline']}")
                        
                            ch = input("Do you want to save this joke as your favourite?")
                            if ch.lower() == "yes":
                                data_j = {
                                    "ID": content['id'],
                                    "Type": "Joke",
                                    "Content": {
                                                "Setup": content['setup'],
                                                "Joke": content['punchline']
                                                }
                                    }
                                fav_list.append(data_j)
                                with open(fav_file, "w") as file:
                                    json.dump(fav_list,file,indent=4)
                                    print("joke saved successfully")
                            else:
                                break

                elif i=="Q" or i=="q":
                
                    while True:
                        response2 = requests.get(Quotes)
                        con = response2.json()
                        if response2.status_code == 200:
                            print(f"Quote: {con['quote']}")
                            print(f"Author: {con['author']}")
                        
                            qh = input("Do you want to save this quote as your favourite?")
                            if qh.lower() == "yes":
                                data_q = {
                                    "ID": con['id'],
                                    "Type": "Quote",
                                    "Content": {
                                                "Quote": con['quote'],
                                                "Author": con['author']
                                                }
                                    }
                                fav_list.append(data_q)
                                with open(fav_file, "w") as file:
                                    json.dump(fav_list,file,indent=4)
                                    print("Quote saved successfully")
                            else:
                                break
                elif i == "e" or i =="E":
                    break

        except Exception as e:
            print(f"Error found: {e}")

    def delete_fav():
        try:
            found = False
            if os.path.exists(fav_file) and os.path.getsize(fav_file)>0:
                with open(fav_file, "r") as file:
                    reader = json.load(file)

            while True:
                jq = input("Enter J or Q to view saved Jokes or Quotes, press E to exit: ")

                if jq == 'J' or jq == 'j':
                    for row in reader:
                        if "Joke" in row['Type']:
                            print(f"ID: {row['ID']}")
                            print(f"Setup: {row['Content']['Setup']}")
                            print(f"Punchline: {row['Content']['Joke']}\n")
                    delj = input("Enter the ID of joke you want to delete: ")
                    fav = [row for row in reader if not (delj == str(row['ID']) and row['Type'] == "Joke")]
                    if len(fav) < len(reader):
                        with open(fav_file, "w") as file:
                            reader = fav
                            json.dump(fav, file, indent=4)
                        print(f"The Joke ID {delj} has been deleted from the file")
                    else:
                        break

                if jq == 'Q' or jq == 'q':
                    for row in reader:
                        if "Quote" in row['Type']:
                            print(f"ID: {row['ID']}")
                            print(f"Setup: {row['Content']['Quote']}")
                            print(f"Punchline: {row['Content']['Author']}\n")
                    delq = input("Enter the ID of Quote you want to delete: ")
                    fav = [row for row in reader if not (delq == str(row['ID']) and row['Type'] == "Quote")]
                    if len(fav) < len(reader):
                        with open(fav_file, "w") as file:
                            reader = fav
                            json.dump(fav,file,indent = 4)
                        print(f"The Quote ID {delq} has been deleted from the file")
                    else:
                        break    

                elif jq == "e":
                    break

                else:
                    print("Invalid key")

        except Exception as e:
            print(f"Error: {e}")

    while True:
        print("JOKE AND QUOTE GENERATOR")
        print("1. Get a random joke")
        print("2. Display Jokes")
        print("3. Get multiple jokes")
        print("4. Get a Quote")
        print("5. Display Quotes")
        print("6. Mark Quote or Joke as Favourite")
        print("7. Delete Favourite Joke or Quote")
        print("8. Quit")

        choice = input("Enter a choice to begin with: ")

        if choice == "1":
            get_random_joke()
        elif choice == "2":
            display_joke()
        elif choice == "3":
            get_multiple_jokes()
        elif choice == "4":
            quote_fetcher()
        elif choice == "5":
            display_quote()
        elif choice == "6":
            save_favourite()
        elif choice == "7":
            delete_fav()
        elif choice == "8":
            break
        else:
            print("Invalid key")


joke()