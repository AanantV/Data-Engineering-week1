import os
import csv
import pandas as pd
from datetime import datetime

def dataframe_exp():

    filename = "Week 2/Day 4/explorer files/employees.csv"
    fn = "Week 2/Day 4/explorer files/reports.txt"

    def load_data(filename):
        try:
            if os.path.exists(filename):
                df = pd.read_csv(filename, sep = ',', encoding = 'utf-8', index_col = 0, header = 0, na_values = ['N/A', 'NaN', 'NA'])
                print(f"Data from the file in path {filename} has been loaded to the dataframe")
                print(f"Number of columns created: {len(df.columns)}")
                print(f"Number of rows created: {len(df.index)}")
                return df

            else:
                print(f"File not found on path: {filename}")

        except Exception as e:
            print(f"File not created: {e}")

    def explore_info(df):
        try: 
            print(f"Shape of the data: {df.shape}")
            print(f"Column names in data: \n{list(df.columns)}")
            print(f"Datatypes of each columns: \n{df.dtypes}")
            print(f"First 5 rows are: ")
            print(df.head(5))
            print(f"Last 5 rows are: ")
            print(df.tail(5))

        except Exception as e:
            print(f"Data explore failed: {e}")

    def check_data_quality(df):
        try:
            print(df.isnull().count())
            missing_percent = (df.isnull().sum()/len(df))*100
            print(f"The missing percentage is: {missing_percent}")
            duplicate = df[df.duplicated()]
            print(f"The number of duplicates are: {len(duplicate)}\nThe duplicates are: \n {duplicate}")
            missing_rows = df[df.isnull().any(axis = 1)]
            print(f"The number of missing rows is: {len(missing_rows)}\nThe Missing rows are: \n{missing_rows}")
            print(df.info(memory_usage = 'deep'))

        except Exception as e:
            print(f"Data Quality Check failed: {e}")

    def show_statistics(df):
        try:
            print(df.describe())
            sorted = df.sort_values(['salary','performance_score'], ascending = False)
            unique = df.drop_duplicates().dropna()
            age_mean = df['age'].mean()
            age_max = df['age'].max()
            age_min = df['age'].min()
            salary_mean = df['salary'].mean()
            salary_max = df['salary'].max()
            salary_min = df['salary'].min()
            performance_mean = df['performance_score'].mean()
            performance_max = df['performance_score'].max()
            performance_min = df['performance_score'].min()

            print(f"Top 10 employees based on score and salary are:")
            print(sorted)
            print(f"Employees with perfect data:")
            print(unique)
            print(f"Mean age: {age_mean}")
            print(f"Maximum age: {age_max}")
            print(f"Minimum age: {age_min}")
            print(f"Mean salary: {salary_mean}")
            print(f"Maximum salary: {salary_max}")
            print(f"Minimum salary: {salary_min}")
            print(f"Mean performance score: {performance_mean}")
            print(f"Maximum performance score: {performance_max}")
            print(f"Minimum performance score: {performance_min}")

        except Exception as e:
            print(f"Statistics Failed: {e}")

    def report(df, fn):
        """Generate comprehensive report and save to file"""
        try:
            with open(fn, "w", encoding='utf-8') as f:
                f.write("="*70 + "\n")
                f.write("           DATAFRAME ANALYSIS REPORT\n")
                f.write("="*70 + "\n")
                f.write(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write(f"File: {filename}\n")
                f.write("="*70 + "\n\n")
            
                f.write("BASIC INFORMATION\n")
                f.write("-"*70 + "\n")
                f.write(f"Shape: {df.shape[0]} rows x {df.shape[1]} columns\n")
                f.write(f"Number of columns: {len(df.columns)}\n")
                f.write(f"Number of rows: {len(df.index)}\n")
                f.write("\n")
            
                f.write("Column Names:\n")
                for i, col in enumerate(df.columns, 1):
                    f.write(f"  {i}. {col}\n")
                f.write("\n")
            
                f.write("Data Types:\n")
                for col, dtype in df.dtypes.items():
                    f.write(f"  {col}: {dtype}\n")
                f.write("\n")
            
                f.write("DUPLICATES\n")
                f.write("-"*70 + "\n")
                duplicate = df[df.duplicated(keep=False)]
                f.write(f"Number of duplicate rows: {len(duplicate)}\n")
            
                if len(duplicate) > 0:
                    f.write("\nDuplicate rows:\n")
                    f.write(str(duplicate))
                    f.write("\n")
                else:
                    f.write("No duplicates found.\n")
                f.write("\n")
            
                f.write("MISSING VALUES\n")
                f.write("-"*70 + "\n")
            
                missing_per_col = df.isnull().sum()
                total_missing = missing_per_col.sum()
            
                f.write(f"Total missing values: {total_missing}\n\n")
            
                f.write("Missing values per column:\n")
                for col, count in missing_per_col.items():
                    if count > 0:
                        pct = (count / len(df)) * 100
                        f.write(f"  {col}: {count} ({pct:.2f}%)\n")
            
                missing_rows = df[df.isnull().any(axis=1)]
                f.write(f"\nNumber of rows with missing values: {len(missing_rows)}\n")
            
                if len(missing_rows) > 0:
                    f.write("\nRows with missing values:\n")
                    f.write(str(missing_rows)) 
                    f.write("\n")
                f.write("\n")
            
                f.write("SUMMARY STATISTICS\n")
                f.write("-"*70 + "\n")
                f.write(str(df.describe()))
                f.write("\n\n")
            
                f.write("="*70 + "\n")
                f.write("           END OF REPORT\n")
                f.write("="*70 + "\n")
        
            print(f"\n Report saved successfully to: {fn}")
        
        except Exception as e:
            print(f"Error generating report: {e}")

    while True:
        print("DATAFRAME EXPLORER SYSTEM")
        print("1. Load Data")
        print("2. Explore Information")
        print("3. Data Quality Check")
        print("4. Statistics")
        print("5. Generate report")
        print("6. Exit")

        choice = input("Enter a valid choice: ")

        if choice == "1":
            load_data(filename)
        elif choice == "2":
            df = load_data(filename)
            if df is not None:
                explore_info(df)
        elif choice == "3":
            df = load_data(filename)
            if df is not None:
                check_data_quality(df)
        elif choice == "4":
            df = load_data(filename)
            if df is not None:
                show_statistics(df)
        elif choice == "5":
            df = load_data(filename)
            if df is not None:
                report(df,fn)
        elif choice == "6":
            print("Quitting...")
            break
        else:
            print("Invalid choice")
        
dataframe_exp()