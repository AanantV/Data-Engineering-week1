import json
import csv
import os
from datetime import datetime

def transaction():
    fn = "Week 2/Day 2/transactions.json"
    filename = "Week 2/Day 2/transactions.csv"
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d, %H-%M-%S")

    def initialise(filename):
        if not os.path.exists(filename):
            with open(filename, "w", newline='') as file:
                writer = csv.DictWriter(file, ['id','date','type','amount','category','description'])
                writer.writeheader()

    def add_transaction():
        try:
            t_list = []
            id = input("Enter the ID: ")
            date = input("Enter date in YYYY-MM-DD format: ")
            income_type = input("Enter the type of income(income/expense): ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")

            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    t_list.append(row)

            transaction = {
                    "id": id,
                    "date": date,
                    "type": income_type,
                    "amount": f"{amount:.2f}",
                    "category": category,
                    "description": description
                }
            t_list.append(transaction)
            
            with open(fn, "w") as file:
                json.dump(t_list, file, indent = 4)

            print(f"transaction for ID: {transaction['id']} is added at {timestamp}")
        
        except Exception as e:
            print(f"JSON Error: {e}")

    def view_transactions():
        try:
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    print(f"Transaction details for {row['id']}")
                    print(f"ID: {row['id']}, Transaction date: {row['date']}, Transaction type: {row['type']}")
                    print(f"Amount spent: {row['amount']}, Category: {row['category']}, Description: {row['description']}\n")

        except Exception as e:
            print(f"JSON Error: {e}")

    def range_transaction():
        try:
            dt = input("Enter the date to view transaction(YYYY/MM/DD): ")
            found = False
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    if row['date'] in dt:
                        print(f"The following users have made transaction on {row['date']}")
                        print(f"ID: {row['id']}, Transaction date: {row['date']}, Transaction type: {row['type']}")
                        print(f"Amount spent: {row['amount']}, Category: {row['category']}, Description: {row['description']}\n")
                        found = True
                if found == False:
                    print(f"There are no transactions available for {dt}")

        except Exception as e:
            print(f"JSON Error: {e}")

    def total_expenses():
        try:
            expense = income = []
            calc = input("What do you want to calculate? Expenses or income? please enter (E/I)")
            with open(fn, "r") as file:
                    reader = json.load(file)
                    if calc == "E":
                            for row in reader:
                                if row['type'] == "expense":
                                    expense.append(float(row['amount']))
                                    sum_e = sum(expense)
                            print(f"The sum of expenses is: {sum_e:.2f}")
                    elif calc == "I":
                            for row in reader:
                                if row['type'] == "income":
                                    expense.append(float(row['amount']))
                                    sum_i = sum(income)
                            print(f"The sum of expenses is: {sum_i:.2f}")
                    else:
                        print("Invalid key.....")
        except Exception as e:
            print(f"JSON Error: {e}")

    def summary():
        try:
            summ = input("What month/day do you want to get a summary report on? please enter in MM format\n for daily in MM-DD: ")
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:    
                    row_dt = datetime.strptime(row['date'], "%Y-%m-%d")
                    row_month = row_dt.strftime("%m")
                    row_date = row_dt.strftime("%m-%d")
                    if row_month == summ:
                        print(f"Transaction for month {summ}")
                        print(f"Transaction ID: {row['id']}\n Amount: {row['amount']}\n Date: {row['date']}\n")
                    elif row_date == summ:
                        print(f"Transaction for daily {summ}")
                        print(f"Transaction ID: {row['id']}\n Amount: {row['amount']}\n Date: {row['date']}\n")
                if row_month != summ or row_date != summ:
                    print("No Transactions found")
                    

        except Exception as e:
            print(f"JSON Error: {e}")

    def export_report():
        try:
            trans = []
            with open(fn, "r") as file:
                reader = json.load(file)
                for row in reader:
                    trans.append(row)
            with open(filename, "w", newline='') as file:
                writer = csv.DictWriter(file, fieldnames = ['id','date','type','amount','category','description'])
                writer.writeheader()
                for row in trans:
                    writer.writerow({'id':row['id'], 'date':row['date'], 'type':row['type'], 'amount': row['amount'], 'category': row['category'], 'description': row['description']})
        except Exception as e:
            print(f"JSON Error: {e}")
    
    initialise(filename)
    
    
    while True:
        print("TRANSACTION MANAGER")
        print("1.Add Transaction")
        print("2.View All Transactions")
        print("3.Range based transaction")
        print("4.Calculate total income/expenses")
        print("5.Daily and Monthly summary")
        print("6.Export report by category")
        print("7.Quit")

        choice = input("Enter the choice: ")

        if choice == "1":
            add_transaction()
        elif choice == "2":
            view_transactions()
        elif choice == "3":
            range_transaction()
        elif choice == "4":
            total_expenses()
        elif choice == "5":
            summary()
        elif choice == "6":
            export_report()
        elif choice == "7":
            break
        else:
            print("Invalid choice")


transaction()