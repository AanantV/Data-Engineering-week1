import csv
import os

def data_cleanup():
    mark = "mark.csv"
    #Read
    def initialize(mark):
        marks = []
        with open(mark, "r") as file:
            marks = csv.reader(file)
            header = next(marks)
            for row in marks:
                print(f"Name: {row[0]}, Physics:{row[1]}, Maths: {row[2]}, Chemistry: {row[3]} ")
    
    #data-clean
    def clean_data(mark):
        try:
            cleaned_data = []
            with open(mark, "r", newline ='') as file:
                reader = csv.reader(file)
                header = next(reader)

                cleaned_data.append(header)
                for row in reader:
                    if '' not in row:
                        cleaned_data.append(row)
                    else:
                        print(f"deleting {row[0]} due to missing values")
            
            with open(mark, "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(cleaned_data)
            
        except Exception as e:
            print(f"No value found: {e}")

    def calculate_data(mark):
        try: 
            max_physics = 0
            max_chemistry = 0
            max_maths = 0
            with open(mark, "r") as file:
                reader = csv.reader(file)
                header = next(reader)

            #calculation.append(header)
                for row in reader:
                    p_mark = int(row[1])
                    c_mark = int(row[2])
                    m_mark = int(row[3])

                    if p_mark > max_physics:
                        max_physics = p_mark
                        p_topper = row[0]
                    if c_mark > max_chemistry:
                        max_chemistry = c_mark
                        c_topper = row[0]
                    if m_mark > max_maths:
                        max_maths = m_mark
                        m_topper = row[0]

                print(f"The highest mark in physics is {max_physics} and the student name is {p_topper}")
                print(f"The highest mark in physics is {max_chemistry} and the student name is {c_topper}")
                print(f"The highest mark in physics is {max_maths} and the student name is {m_topper}")
        
        except Exception as e:
            print(f"No data found: {e}")
    filename = "cleaned.csv"
    def save_cleaned_data(mark, filename):
        clean_data(mark)
        try:
            fieldname = ["Name", "Physics","Maths", "Chemistry"]
            if not os.path.exists(filename):
                with open(filename , "w", newline = '') as file:
                    writer = csv.DictWriter(file, fieldnames = fieldname)
                    writer.writeheader()
            marks = []
            with open(mark, "r") as file:
                reader = csv.reader(file)
                for marks in reader:
                    with open(filename, "a") as file:
                        writer = csv.writer(file)
                        writer.writerows()


        except Exception as e:
            print(f"No file found: {e}")
                
            
        

    #initialize(mark)
    #clean_data(mark)
    #calculate_data(mark)
    save_cleaned_data(mark, filename)


data_cleanup()