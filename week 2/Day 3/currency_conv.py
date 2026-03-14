import requests
import json
import os
from datetime import datetime, timedelta

def currency():

    url = "https://api.exchangerate-api.com/v4/latest/USD"
    filename = "Week 2/Day 3/output files/exchange_rates_cache.json"
    filename1 = "Week 2/Day 3/output files/refresh_exchange_rates_cache.json"
    filename2 = "Week 2/Day 3/output files/conversion_history.json"

    now  = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")

    response = requests.get(url)
    response.raise_for_status()
    
    if response.status_code == 200:
        data = response.json()

    def get_exchange_rates(bc):
        try:
            target = data['rates']
            for k in target:
                if k in bc:
                    print(f"{bc} : {target[bc]}")

        except Exception as e:
            print(f"Error found: {e}")
        return None
    
    def cache_rates(r):
        try:
            content = data['rates']
            last_updated = data['time_last_updated']
            unix_to_time = datetime.fromtimestamp(last_updated)
            r_dt = datetime.strptime(r, "%Y-%m-%d %H:%M:%S")
            r_time = r_dt - timedelta(hours = 1)
        
            response1 = requests.get(url)
            if response1.status_code == 200:
                if unix_to_time < r_time:
                    latest = {
                  "Last updated time": r,
                  "Currency": content  
                    }
                    with open(filename, "w") as file:
                        json.dump(latest,file, indent=4)
        
        except Exception as e:
            print(f"Error found: {e}")

    
    def load_cached_rates():

        try:
            needs_refresh = True

            r = timestamp
            r_dt = datetime.strptime(r, "%Y-%m-%d %H:%M:%S")
            r_time = r_dt- timedelta(hours =1)
            if os.path.exists(filename) and os.path.getsize(filename) > 0:
                with open(filename, "r") as file:
                    cache_data = json.load(file)
        
            cache_time_str = cache_data.get("Last updated time")
            cache_time = datetime.strptime(cache_time_str, "%Y-%m-%d %H:%M:%S")
        
            if cache_time > r_time:
                content = cache_data['Currency']
                with open(filename1, "w") as file:
                        json.dump(cache_data, file, indent=4)
                needs_refresh = False

            if needs_refresh:
                if response.status_code == 200:
                    data = response.json()
                    content = data['rates']

                    latest = {
                    "Refresh time": timestamp,
                    "Currency": content
                    }

                    with open(filename1, "w") as file:
                        json.dump(latest, file, indent =4)
                print(f"Data refreshed at {timestamp} and loaded to {filename1}")

        except Exception as e:
            print(f"Error found: {e}")

    def convert_currency(amount, from_currency, to_currency): 
        amt = float(amount)
        from_curr = from_currency.upper()
        to_curr = to_currency.upper()
        try: 
            if len(from_curr) != 3 or len(to_curr) != 3:
                print("Invalid value")
        
            load_cached_rates()

            if not os.path.exists(filename1) or os.path.getsize(filename1) == 0:
                print("Rates data is currently unavailable.")
                return

            with open(filename1, "r") as file:
                cached_data = json.load(file)

            currency = cached_data.get("Currency",{})
            if from_curr in currency and to_curr in currency:
                amt_f = float(currency[from_curr])
                amt_t = float(currency[to_curr])
                conv_amt = (amt/amt_f)*amt_t
                conv_a = float(f"{conv_amt:.2f}")

                print(f"The converted amount from {from_curr} to {to_curr} is {conv_a}")

                curr_history = []
                if os.path.exists(filename2):
                    with open(filename2, "r") as file:
                        try:
                            curr_history = json.load(file)
                        except json.JSONDecodeError: 
                            curr_history = []
                content = {
                "Amount": amt,
                "From": from_curr,
                "To": to_curr,
                "Result": conv_a
            }
                curr_history.append(content)

                with open(filename2, "w") as file:
                    json.dump(curr_history, file, indent=4)
                print(f"History updated in {filename2}")
            else:
                print(f"Error: {from_curr} or {to_curr} not found in rates.")

        except Exception as e:
            print(f"Error Found: {e}")

    def display_currency(base_currency):

        try:
            if not os.path.exists(filename2) or os.path.getsize(filename2) == 0:
                print("No conversion history available.")
                return
            
            with open(filename1, "r") as file:
                reader = json.load(file)
                content = reader.get("Currency", {})
            if base_currency in content:
                print(f"The rate for {base_currency} is {content[base_currency]}")
            else:
                print("Invalid currency code")
     
        except Exception as e:
            print(f"Error found : {e}")

    def saved_data():
        try:
            with open(filename1, "r") as file:
                reader = json.load(file)
                content = reader.get("Currency", {})
                for k,v in content.items():
                    print(f"Currency code: {k} -------> Rate: {v}")
                
        except Exception as e:
            print(f"Error found: {e}")

    def conversion_history():
        try:
            with open(filename2, "r") as file:
                reader = json.load(file)
                for row in reader:
                    print(f"Amount: {row['Amount']}")
                    print(f"Converted from: {row['From']}")
                    print(f"Converted to: {row['To']}")
                    print(f"Result: {row['Result']}\n")

        except Exception as e:
            print(f"Error found: {e}")


    while True:
        print("CURRENCY CONVERTER")
        print("1. View Exchange Rates")
        print("2. Convert Currency")
        print("3. Conversion History")
        print("4. Refresh Rates")
        print("5. Specific Currency Rate")

        choice = input("Enter a valid choice: ")

        if choice == "1":
            saved_data()

        elif choice == "2":
                amount = input("Enter the amount: ")
                from_currency = input("Enter the 3-digit country code of the amount: ")
                to_currency = input("Enter the 3-digit country code for the amount conversion:")
                convert_currency(amount, from_currency, to_currency) 
        elif choice == "3":
            conversion_history()
        elif choice == "4":
            load_cached_rates()
        elif choice == "5":
           base_currency = input("Enter the currency code you want to view: ")
           display_currency(base_currency)
        elif choice == "6":
            break
        else:
            print("Invalid choice")

currency()