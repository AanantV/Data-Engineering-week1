import requests
import os
import json
from datetime import datetime
from collections import Counter

def random_user():

    url = "https://randomuser.me/api"

    filename = "Week 2/Day 3/Random_user_files/Random_user.json"
    user_json = "Week 2/Day 3/Random_user_files/users.json"

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    def generate_user():
        try:
            count = int(input("Enter the Number of users you want to generate: "))
            Parameters = {
            "results" : count
            }

            response = requests.get(url, params= Parameters)
            response.raise_for_status()
            if response.status_code == 200:
                data = response.json()
            users = []
            total_cnt = len(data['results'])

            gender = data['results']
            m_count = f_count =0

            for c in gender:
                if c['gender'] == "male":
                    m_count += 1
                if c['gender'] == "female":
                    f_count += 1

            if os.path.exists(filename):
                with open(filename, "r") as file:
                    users = json.load(file)

                load = {
                    "Generated at": timestamp,
                    "Count": total_cnt,
                    "Male Count": m_count,
                    "Female Count": f_count
                        }
                
                users.append(load)
                
                with open(filename, "w") as file:
                    json.dump(users, file, indent = 4)

            total_users = []
            #Name, Email, Age, Gender, Nationality, Location
            user = data['results']
            for row in user:
                name = f"{row['name']['title']} {row['name']['first']} {row['name']['last']}"
                email = row['email']
                age = row['dob']['age']
                gender = row['gender']
                nationality = row['location']['country']
                location = f"{row['location']['street']['number']} {row['location']['street']['name']}"

                user_info = {
                    "name": name,
                    "email" : email,
                    "age": age,
                    "gender": gender,
                    "nationality": nationality,
                    "location": location
                }

                total_users.append(user_info)

            try:
                if os.path.exists(user_json):
                    with open(user_json, "w") as file:
                        json.dump(total_users,file,indent = 4)

            except Exception as e:
                print(f"File not created: {e}")    

        except Exception as e:
            print(f"Error found: {e}")

    def display():
        try:
            if os.path.exists(user_json):
                with open(user_json, "r") as file:
                    reader = json.load(file)
                    print("USERS LIST")
                    for row in reader:
                        
                        print(f"\nName: {row['name']}")
                        print(f"Email: {row['email']}")
                        print(f"Age: {row['age']}")
                        print(f"Gender: {row['gender']}")
                        print(f"Location: {row['location']}")
                        print(f"Nationality: {row['nationality']}\n")
            

        except Exception as e:
            print(f"Error found: {e}")

    def analyze_demographics():
        try:
            if os.path.exists(user_json):
                with open(user_json, "r") as file:
                    reader = json.load(file)
                    male_c = female_c = count18 = count26 = count36 = count51 = 0
                    nationality = []
                    age = []
                    for row in reader:
                        
                        if 'male' in row['gender']:
                            male_c += 1
                        if 'female' in row['gender']:
                            female_c += 1
                        if row['age'] >=18 and row['age']<=25:
                            count18 +=1
                        if row['age'] >=26 and row['age']<=35:
                            count26 +=1
                        if row['age'] >=36 and row['age']<=50:
                            count36 +=1
                        if row['age'] >=51:
                            count51 +=1
                        nationality.append(row['nationality'])
                        age.append(row['age'])
                    print(f"The Male count is: {male_c}")
                    print(f"\nThe female count is: {female_c}")
                    
                    count = Counter(nationality)
                    print("\nThe Nationality wise count is:\n")
                    for ke, v in count.items():
                        print(f"Country: {ke}, count: {v}")
                    print("\n Age wise break up:")
                    print(f"\nCount of individuals in age group 18-25 is: {count18}")
                    print(f"Count of individuals in age group 26-35 is: {count26}")
                    print(f"Count of individuals in age group 36-50 is: {count36}")
                    print(f"Count of individuals in age group greater than 51 is: {count51}")

                    age_avg = sum(age)/len(age)
                    avg_age = round(age_avg,2)
                    print(f"The average based on age is: {avg_age}")

        except Exception as e:
            print(f"Error found: {e}")

    def search_by_country():
        try:
            country = input("Enter the Country name to display the users: ")
            count = []
            if os.path.exists(user_json):
                with open(user_json, "r") as file:
                    reader = json.load(file)
                    for row in reader:
                        if country in row['nationality']:
                            print(f"The Country matched with the data....")
                            name = row['name']
                            address = row['location']
                            nationality = row['nationality']

                            content = {
                                "Name": name,
                                "Address": address,
                                "Nationality": nationality
                            }

                            count.append(content)

                    print(f"\nThe count of users present in {country} is {len(count)} \n The Users are...")
                    for n in count:
                        print(f"Name: {n['Name']}")
                        print(f"Address: {n['Address']}")
                        print(f"Nationality: {n['Nationality']}\n")

        except Exception as e:
            print(f"Error found: {e}")

    def load_data():
        try:
            if os.path.exists(user_json):
                with open(user_json, "r") as file:
                    reader = json.load(file)
                    print("USERS LIST")
                    for row in reader:
                        
                        print(f"\nName: {row['name']}")
                        print(f"Email: {row['email']}")
                        print(f"Age: {row['age']}")
                        print(f"Gender: {row['gender']}")
                        print(f"Location: {row['location']}")
                        print(f"Nationality: {row['nationality']}\n")

        except Exception as e:
            print(f"Error found: {e}")


    while True:

        print("CURRENCY CONVERTER")
        print("1. Generate User")
        print("2. Display Users")
        print("3. Analysis")
        print("4. Country Based Users")
        print("5. Load all users from JSON file")
        print("6. Quit")

        choice = input("Enter a valid choice: ")

        if choice == "1":
            generate_user()
        elif choice == "2":
            display()     
        elif choice == "3":
            analyze_demographics()
        elif choice == "4":
            search_by_country()
        elif choice == "5":
            load_data()
        elif choice == "6":
            break
        else:
            print("Invalid choice")

random_user()