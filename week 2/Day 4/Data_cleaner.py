import os
from datetime import datetime
import pandas as pd
import numpy as np

def data_cleaner():

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d%H%M%S")

    filename = "Week 2/Day 4/Data_cleaner_files/employees.csv"
    updates = f"Week 2/Day 4/Data_cleaner_files/cleaned_{timestamp}.csv"


    def get_data(filename):
        try:
            if os.path.exists(filename):
                df = pd.read_csv(filename, sep=',', encoding = 'utf-8', header = 0, na_values = ['NaN','N/A', 'NA'], index_col = 0)
                df = df.replace(['NaN', 'nan', 'NaN ', ' nan', 'None', 'n/a'], np.nan)
                return df
        except Exception as e:
            print(f"File not found: {e}")

    def load_messy_data(df):
        try:
            print(f"Shape of Data: {df.shape[0]} rows x {df.shape[1]} columns")
            print(f"Data Info:")
            print(df.info())
            print(df)
        except Exception as e:
            print(f"Data load failed: {e}")

    def find_missing_values(df):
        try:
            missing = df[df.isnull().any(axis=1)]
            missing_per = (df.isnull().sum()/len(df))*100
            print(f"The values missing in total is: {len(missing)}")
            print(f"Missing percentage based on rows:\n{missing_per}")
            print("Rows with missing data:")
            print(missing)
            return missing

        except Exception as e:
            print(f"Missing values can't be found: {e}")

    def handle_missing_values(df):
        try:
            missing = df.isnull().sum().sort_values(ascending = True)
            while True:
                print("Missing values column wise:")
                print(missing)
                print("1. Drop rows writh missing values")
                print("2. Fill with mean(numeric only)")
                print("3. Fill with median(numeric only)")
                print("4. Fill with mode(categorical)")
                print("5. Fill with custom value")
                print("6. Return Updated dataframe")

                choice = input("Enter the operation you want to perform: ")

                if choice == "1":
                    initial_len = len(df)
                    df = df.dropna()
                    print(f"Number of rows dropped: {initial_len - len(df)}")
                    print(df)
                elif choice == "2":
                    print(df.dtypes)
                    print(df)
                    col = input("Enter the name of column you want to perform the action: ")
                    df[col] = df[col].fillna(df[col].mean())
                    print(f"Missing values remaining in {col}: {df[col].isnull().sum()}")
                    print(df.isnull().sum())
                elif choice == "3":
                    print(df.dtypes)
                    col = input("Enter the name of column you want to perform the action: ")
                    df[col] = df[col].fillna(df[col].median())
                    print(f"Missing values remaining in {col}: {df[col].isnull().sum()}")
                    print(df.isnull().sum())
                elif choice == "4":
                    print(df.dtypes)
                    col = input("Enter the name of the column you want to perform the action: ")
                    df[col] = df[col].fillna(df[col].mode()[0])
                    print(f"Missing values remaining in {col}: {df[col].isnull().sum()}")
                    print(df.isnull().sum())
                elif choice == "5":
                    print(df.dtypes)
                    col = input("Enter the name of the column you want to perform the action: ")
                    print("Do you want to replace it for a single or multiple values")
                    ch = input("For single press 'S', For multiple press 'M': ")
                    if ch == 'S' or ch == 's':
                        print(df.loc[df[col].isnull(),'name'])
                        name = input("Enter the name of the user: ")
                        val = input("Enter the value: ")
                        try:
                            if '.' in val:
                                val = float(val)
                            else:
                                val = int(val)
                        except ValueError:
                            pass
                        if name.lower().strip() in df['name'].str.lower().str.strip().values:
                            df.loc[df['name'].str.lower().str.strip() == name.lower().strip(), col] = val
                            print(f"The value {val} has been mapped to user {name} in column {col}")
                            print(df)
                        else:
                            print("Unable to map the value")
                    elif ch == 'M' or ch == 'm':
                        print(df.dtypes)
                        col = input("Enter the column you want to populate the values: ")
                        val = input("Enter the value to be populated: ")
                        try:
                            if '.' in val:
                                val = float(val)
                            else:
                                val = int(val)
                        except ValueError:
                            pass
                        df[col] = df[col].fillna(val)
                        print(df)

                elif choice == "6":
                    return df
                else:
                    print("Invalid value")

        except Exception as e:
            print(f"Handling null values failed: {e}")

    def remove_duplicates(df):
        try:
            duplicates = df[df.duplicated()]
            if len(duplicates) > 0:
                print("Duplicate value(s) found!!")
                print(f"Number of duplicates: {len(duplicates)}")
                print("DUPLICATE VALUE:")
                print(duplicates)
                i = input("Do you want to delete the duplicate? type 'Y' for yes and 'N' for no: ")
                if i.lower() == 'y':
                    df = df.drop_duplicates()
                    print("Duplicate is removed")
                else:
                    print("No duplicates found")
                return df
        except Exception as e:
            print(f"Duplicate removal failed: {e}")

    def convert_data_types(df):
        try:
            print(df.dtypes)
            col = input("Enter the column datatype you want to change: ")
            datatype = input("Enter the datatype for int press 'i', for float press 'f', for datetime press 'd': ")
            if datatype == 'i':
                df[col] = df[col].astype("Int64")
                print(f"The datatype of {col} is changed to int")
                print(f"{col}: {df[col].dtypes}")
            elif datatype == 'f':
                df[col] = df[col].astype(float)
                print(f"The datatype of {col} is changed to float")
                print(f"{col}: {df[col].dtypes}")
            elif datatype == 'd':
                df[col] = pd.to_datetime(df[col])
                print(f"The datatype of {col} is changed to datetime")
                print(f"{col}: {df[col].dtypes}")
            else:
                print("No transformations performed")
            return df

        except Exception as e:
            print(f"Data type conversion failed: {e}")

    def save_cleaned_data(df, updates):
        try:
            df.to_csv(updates, index = True)
            print(f"Cleaned Data saved on path: {updates}")
            total_nulls_left = df.isnull().sum().sum()
            print(f"Total Nulls Remaining: {total_nulls_left}")

        except Exception as e:
            print(f"Data Save failed: {e}")

    data = get_data(filename)
    if data is None:
        print("Failed to load initial data. Exiting.")
        return

    while True:
        print("*****DATA CLEANER*****")
        print("1. Load messy data")
        print("2. Find missing values")
        print("3. Clean data")
        print("4. Remove duplicates")
        print("5. Convert data types")
        print("6. Saving cleaned data")
        print("7. Quit")

        choice = input("Enter a valid choice: ")

        if choice == "1":
            load_messy_data(data)
        elif choice == "2":
            find_missing_values(data)
        elif choice == "3":
            data = handle_missing_values(data)
            print("Cleaned up the data")
        elif choice == "4":
            data = remove_duplicates(data)
        elif choice == "5":
           data = convert_data_types(data)
        elif choice == "6":
           if data is not None:
                save_cleaned_data(data, updates)
        elif choice == "7":
            print("Quitting...")
            break
        else:
            print("Invalid choice")
 
data_cleaner()
