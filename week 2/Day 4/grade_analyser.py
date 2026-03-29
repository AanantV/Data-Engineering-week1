import pandas as pd
import numpy as np
import os

def grade_analysis():

    filename = "Week 2/Day 4/grade files/grades.csv"
    xl = "Week 2/Day 4/grade files/grades.xlsx"

    def get_students(filename):
        try:
            if os.path.exists(filename):
                df = pd.read_csv(filename, sep=",", header = 0, index_col = 0, encoding = 'utf-8', na_values = ['NaN', 'N/A', "NA"])
                df.replace(['NaN','nan','None','NA','NAN','N/A'],np.nan)
                return df

        except Exception as e:
            print(f"File access failed: {e}")

    def load_students(df):
        try:
            print(f"Shape of the data: {df.shape[0]}rowsx{df.shape[1]}columns\n")
            print(f"Number of rows: {len(df.index)}\n")
            print(f"Student Names(rows):\n")
            rows = df.index.tolist()
            for i in rows:
                print(i)
            print(f"\nNumber of columns: {len(df.columns)}\n")
            print("Columns:\n")
            columns = df.columns.tolist()
            for j in columns:
                print(j)
            print(df.dtypes)
            return df

        except Exception as e:
            print(f"Student load failed: {e}")

    def add_student(df):
        try:
            name = input("\nEnter the student name: ")
            age = int(input("Enter the age: "))
            test1 = int(input("Enter the score for test 1: "))
            test2 = int(input("Enter the score for test 2: "))
            test3 = int(input("Enter the score for test 3: "))

            new_data = [[age,test1,test2,test3]]
            new_row_df = pd.DataFrame(new_data, columns = ['age','test1','test2','test3'], index = [name])
            df = pd.concat([df,new_row_df])

            # df.loc[name] = [age, test1, test2, test3]---alternative
            print(df)

            print(f"Student {name} has been added to the database")
            print(f"Shape of data after adding new student: {df.shape}")

            return df

        except Exception as e:
            print(f"Unable to add student: {e}")
            return df
        
    def calculate_averages(df):
        try:
            df['average'] = (df['test1']+df['test2']+df['test3'])/3
            df['average'] = df['average'].round(2)
            print("Average calculations have been performed and column is added")
            print(df)
            return df

        except Exception as e:
            print(f"Average Calculation failed: {e}")

    def add_letter_grades(df):
        try:
            bins = [0,50,60,70,80,90,100]
            labels = ['F','E','D','C','B','A']
            df['grade'] = pd.cut(df['average'], bins = bins, labels = labels, include_lowest = True)
            print("Grade column added: Updated dataframe\n")
            print(df)
            return df

        except Exception as e:
            print(f"Letter grade cannot be added: {e}")

    def filter_by_grade(df,letter_grade):
        try:
            avg = calculate_averages(df)
            grade = add_letter_grades(avg)
            fil = grade[grade['grade'] == letter_grade.upper()]
            sort_df = fil.sort_values(['average'], ascending = False)
            print("Sorted students based on provided grade:")
            print(sort_df)
            return sort_df

        except Exception as e:
            print(f"Grade filter failed: {e}")

    def top_student(df, n):
        try:
            df['average'] = (df['test1']+df['test2']+df['test3'])/3
            df['average'] = df['average'].round(2)
            sort = df.sort_values(['average'], ascending = False)
            print(f"Top {n} students")
            print(sort.head(n))
            return sort

        except Exception as e:
            print(f"Student sorting failed: {e}")

    def calculate_statistics(df):
        try:
            avg = calculate_averages(df)
            grade = add_letter_grades(avg)
            print("Class Average:")
            print(avg['average'].mean())
            print("\nTest 1 statistics: ")
            top_student1 = avg['test1'].idxmax()
            last_student1 = avg['test1'].idxmin()
            top_student2 = avg['test2'].idxmax()
            last_student2 = avg['test2'].idxmin()
            top_student3 = avg['test3'].idxmax()
            last_student3 = avg['test3'].idxmin()
            print(f"Maximum score: {avg['test1'].max()} Student Name: {top_student1}")
            print(f"Minimum score: {avg['test1'].min()} Student Name: {last_student1}")
            print("\nTest 2 statistics: ")
            print(f"Maximum score: {avg['test2'].max()} Student Name: {top_student2}")
            print(f"Minimum score: {avg['test2'].min()} Student Name: {last_student2}")
            print("\nTest 3 statistics: ")
            print(f"Maximum score: {avg['test3'].max()} Student Name: {top_student3}")
            print(f"Minimum score: {avg['test3'].min()} Student Name: {last_student3}")
            print("\nGrade statistics: ")
            print(grade['grade'].value_counts())


        except Exception as e:
            print(f"Statistics calculation failed: {e}")

    def save_excel(df, xl):
        try:
            if 'average' not in df.columns:
                df = calculate_averages(df)
            if 'grade' not in df.columns:
                df = add_letter_grades(df)
            user_grade = input("Enter grade to filter for the 'Filtered' sheet: ")
            filtered = filter_by_grade(df, user_grade)

            with pd.ExcelWriter(xl, engine = 'openpyxl') as writer:

                df.to_excel(writer, sheet_name = 'Complete_Report', index = True)
                if 'F' in df['grade'].values:
                    df[df['grade'] == 'F'].to_excel(writer, sheet_name='Action_Required')
                if filtered is not None:
                    filtered.to_excel(writer, sheet_name='Filtered_Results', index=True)
                print(f"\nSuccessfully saved all reports to {xl}")

        except Exception as e:
            print(f"Excel save failed: {e}")

    data = get_students(filename)
    if data is None:
        print("Failed to load initial data.")
        return

    while True:
        print("*****STUDENT GRADE SYSTEM*****")
        print("1. Load Students data")
        print("2. Add Student")
        print("3. Average")
        print("4. Letter Grade")
        print("5. Grade Sorting")
        print("6. Subject wise top students")
        print("7. Class statistics")
        print("8. Save Excel")
        print("9. Quit")

        choice = input("Enter a valid choice: ")

        if choice == "1":
            load_students(data)
        elif choice == "2":
            data = add_student(data)
        elif choice == "3":
            data = calculate_averages(data)
        elif choice == "4":
            data = calculate_averages(data)
            data = add_letter_grades(data)
        elif choice == "5":
            letter = input("Enter the grade(A,B,C,D,E): ")
            filter_by_grade(data, letter)
        elif choice == "6":
            n = int(input("Enter a number to view top students: "))
            top_student(data, n)
        elif choice == "7":
            calculate_statistics(data)
        elif choice == "8":
            save_excel(data, xl)
        elif choice == "9":
            print("Quitting...")
            break
        else:
            print("Invalid choice")

grade_analysis()