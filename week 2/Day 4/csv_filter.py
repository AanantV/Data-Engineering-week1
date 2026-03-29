import os
import pandas as pd
import numpy as np
import json
import textwrap

def csv_filter():

    filter_file = "Python-practice/week 2/Day 4/csv filter files/filter_history.json"
    
    def get_data(filename):
        try:
            df = pd.read_csv(filename, sep = ',', index_col = 0, header = 0, na_values = ['NaN', 'N/A', 'NA'])
            df = df.replace(['nan','NAN', 'NaN', 'None', 'N/A', 'n/a'],np.nan)
            df['Phone'] = df['Phone'].str.lstrip("+1").str.split('x').str[0].str.replace(r'[+\-.\(\)]','',regex = True).astype(int)
            df['Date of birth'] = pd.to_datetime(df['Date of birth'], errors = ('coerce'))
            return df

        except Exception as e:
            print(f"Unable to access file: {e}")

    def load_file(df):
        try:
            print(f"Shape of the data: {df.shape[0]}rows x {df.shape[1]}columns")
            print("\nData types of each columns:")
            print(df.dtypes)
            print("\nColumns:")
            for v in df.columns:
                print(v)
            print("\nData preview:")
            print(df.head(5))
            return df

        except Exception as e:
            print(f"Data Load operation failed: {e}")

    def apply_filters(df):
        try:
            filter_info = {}
            word = ch = col = None
            count = 0
            cols_filtered = []
            print("\nINTERACTIVE FILTER")
            print("\nAvailable columns:")
            print(df.head(5))
            print(df.dtypes)
            result = df
            count = int(input("How many filters you want to apply?: "))
            while count>0:
                col = input("Enter the name of the column you want to apply for: ")
                cols_filtered.append(col)
                if col in df.columns and df[col].dtypes == "int64":
                    ch = int(input("Enter the number to be found: "))
                    result = result[result[col] == ch]
                    print("User found")
                    for index, row in result.iterrows():
                        name = row['First Name']+" "+row['Last Name']
                        print(f"Name: {name}")
                        print(f"Gender: {row['Sex']}")
                        print(f"Email: {row['Phone']}")
                        print(f"DOB: {row['Date of birth']}")
                        print(f"Job Title: {row['Job Title']}")

                elif col in df.columns and df[col].dtypes == "object":
                    while True:
                        print("1. Find values that contain")
                        print("2. Starts with")
                        print("3. Ends with")
                        print("4. Exact Value")
                        print("5. Quit")
                        op = input("Select a choice to perform operation:")

                        if op == "5":
                            break

                        if op == "1":
                            word = input("Enter the word to proceed: ")
                            result = result[result[col].str.contains(word)]  

                        elif op == "2":
                            word = input("Enter the word to proceed: ")
                            result = result[result[col].str.startswith(word)]
                    
                        elif op == "3":
                            word = input("Enter the word to proceed: ")
                            result = result[result[col].str.endswith(word)]  
                    
                        elif op == "4":
                            word = input("Enter the word to proceed: ")
                            result = result[result[col]==word]
                            
                        else:
                            print("Invalid value")
                            continue
                        break
                
                else:
                    print("Element access failed")

                count-=1

            filter_info = {
                "Function name": "Apply_filters",
                "Filter count": len(cols_filtered),
                "Filter applied on columns": cols_filtered,
                "Numeric filter": ch,
                "String filter": word
            }

            print(result)
            return result,filter_info

        except Exception as e:
            print(f"Filter apply failed: {e}")
    
    def select_columns(df):
        try:
            num = []
            na = []
            all_used = False
            numeric_used = False
            name_used = False
            print("Available columns from the System:")
            i=0
            for v in df.columns:
                    print(f"{i+1}. {v}")
                    i+=1
            while True:
                ch = input("To view all columns press 'A', by number press 'N', by Name press 'T', to quit press 'Q': ")
                if ch.upper() == 'A':
                    print(df)
                    all_used = True
                elif ch.upper() == 'N':
                    indices = input('Enter the numbers of columns you want to view(eg: 3,5,6): ')
                    selected_col = [df.columns[int(i)-1] for i in indices.split(',')]
                    print(df[selected_col])
                    num.extend(selected_col)
                    numeric_used = True
                elif ch.upper() == 'T':
                    name = input("Enter the name of the column: ")
                    if name in df.columns:
                        print(df[name])
                        na.append(name)
                        name_used = True
                elif ch.upper() == 'Q':
                    print("Quitting...")
                    break
                else:
                    print("Invalid choice")
            select_info = {
                "function_name": "Select Columns",
                "All column selection": all_used,
                "All Columns affected": "All" if all_used == True else None,
                "Numeric Selection": numeric_used,
                "Numeric Columns affected": num if numeric_used ==  True else None,
                "Name Selection": name_used,
                "Name Columns affected": na if name_used == True else None
            }
            return df,select_info

        except Exception as e:
            print(f"Column selection failed: {e}")

    def sort_data(df):
        try:
            col_name = None
            col_names = []
            uni = False
            multi = False
            asc = False
            desc = False
            m_asc = False
            m_desc = False
            li = []
            i=0
            print("Available columns from file: ")
            for v in df.columns:
                print(f"{i+1}. {v}")
                i+=1
            while True:
                ch = input("For Uni-sort type 'S', For Multi-sort type 'M', To quit type 'Q': ")
                if ch == 'S':
                    uni = True
                    num = int(input("Enter a column number to sort by: "))
                    s = input("Enter the sort type (asc/desc): ")
                    if s == 'asc':
                        print(f"Sorted data by {df.columns[num-1]} on ascending")
                        sort = df.sort_values(df.columns[num-1], ascending = True)
                        col_name = df.columns[num-1]
                        asc = True
                        print(sort)
                    elif s == 'desc':
                        print(f"Sorted data by {df.columns[num-1]} on Descending")
                        sort = df.sort_values(df.columns[num-1], ascending = False)
                        col_name = df.columns[num-1]
                        uni = True
                        desc = True
                        print(sort)
                    else:
                        print("Invalid sort type")
                elif ch == 'M':
                    multi = True
                    n = input("Enter the number of columns (2,3,4): ")
                    s = input("Enter the sort type (asc/desc): ")
                    num_str = n.split(',')
                    if s == 'asc':
                        m_asc = True
                        li = [int(i) for i in num_str]
                        col_names = [df.columns[j-1] for j in li]
                        sort = df.sort_values(col_names, ascending=True)
                    elif s == 'desc':
                        m_desc = True
                        li = [int(i) for i in num_str]
                        col_names = [df.columns[j-1] for j in li]
                        sort = df.sort_values(col_names, ascending=False)
                    
                    print(f"Sorted columns based on Selected Columns: ")
                    print(sort)
                elif ch == 'Q':
                    print("Quitting...")
                    break
                else:
                    print("Invalid choice")
            sort_info = {
                "Sort type": {
                    "Type": "Unisort" if uni else "Multisort" if multi else None,
                    "Unisort info":{"Order": {
                        "Ascending": asc,
                        "Descending": desc
                    },
                    "Column affected in Unisort": col_name if uni else None
                    },
                    "Multisort info":{"Order": {
                        "Ascending": m_asc,
                        "Descending": m_desc
                    },
                    "Column affected in Multisort": col_names if multi else None
                    }
                }
            }
            return df,sort_info

        except Exception as e:
            print(f"Sorting failed: {e}")
    
    def export_data(df):
        try:
            file_df = df
            print("What format do you want to save the data?\n1.CSV\n2.JSON\n3.Excel")
            ch = input("Enter the number: ")
            if ch == '1':
                fn = input("Enter file name (with .csv): ")
                p = "Python-practice/week 2/Day 4/csv filter files"
                fnn = os.path.join(p,fn).replace('\\','/')
                file_df.to_csv(fnn, index = False)
                print(f"File Saved on Path: {fnn}")
            elif ch == '2':
                fn = input("Enter file name (with .json): ")
                p = "Python-practice/week 2/Day 4/csv filter files"
                fnn = os.path.join(p,fn).replace('\\','/')
                file_df.to_json(fnn, orient = 'records',indent =4)
                print(f"File Saved on Path: {fnn}")
            elif ch == '3':
                fn = input("Enter file name (with .xlsx): ")
                p = "Python-practice/week 2/Day 4/csv filter files"
                fnn = os.path.join(p,fn).replace('\\','/')
                file_df.to_excel(fnn, index = False)
                print(f"File Saved on Path: {fnn}")
            else:
                print("Invalid choice")
            return file_df,fnn

        except Exception as e:
            print(f"Data Export failed: {e}")

    def save_filter(filter_info, select_info, sort_info):
        try:
            if not filter_info and not select_info and not sort_info:
                print("No filters applied yet. Run options 2, 3, or 4 first.")
                return

            li = [filter_info,select_info,sort_info]

            if not os.path.exists(filter_file):
                with open(filter_file, "w") as file:
                    json.dump(li, file, indent = 4)
                print(f"History Saved on Path: {filter_file}")

            if os.path.exists(filter_file):
                with open(filter_file, "w") as file:
                    json.dump(li, file, indent = 4)
                print(f"History Saved on Path: {filter_file}")

        except Exception as e:
            print(f"Filter save failed: {e}")


    def preview_data(fnn):
        try:
            if not fnn:
                print("No file has been created yet. Run option 5 first.")
                return
            
            file_df = pd.read_csv(fnn, sep = ',', index_col = 0, header = 0, na_values = ['NaN', 'N/A', 'NA'])
            file_df = file_df.replace(['nan','NAN', 'NaN', 'None', 'N/A', 'n/a'],np.nan)
            n = int(input("Enter the number of rows: "))
            print(f"Data preview of first {n} rows:")
            print(file_df.head(n))
            print(f"Shape of data: {file_df.shape}") 
            print("Columns in the file:")
            for col in file_df.columns:
                print(f"- {col}")
            return None

        except Exception as e:
            print(f"Data Preview Failed: {e}")
        
    fn = input("Enter the filename(with .csv): ")
    path = "Python-practice/week 2/Day 4/csv filter files"
    filename = os.path.join(path, fn).replace('\\','/')
    
    data = get_data(filename)

    if data is None:
        print("Failed to load initial data.")
        return
    
    filter_info = {}
    select_info = {}
    sort_info = {}
    fnn = None


    while True:
        print("*****CSV FILTER SYSTEM*****")
        print("1. Load data")
        print("2. Apply Filters")
        print("3. Select Columns")
        print("4. Sort Data")
        print("5. Export Data")
        print("6. Save Filter History")
        print("7. Data Preview")
        print("8. Quit")

        choice = input("Enter a valid choice: ")

        if choice == "1":
            load_file(data)
        elif choice == "2":
            data, filter_info = apply_filters(data)
        elif choice == "3":
            data, select_info = select_columns(data)
        elif choice == "4":
            data, sort_info = sort_data(data)
        elif choice == "5":
            data, fnn = export_data(data)
        elif choice == "6":
            save_filter(filter_info,select_info,sort_info)
        elif choice == "7":
            preview_data(fnn)
        elif choice == "8":
            print("Quitting...")
            break
        else:
            print("Invalid choice")

csv_filter()