from datetime import datetime
import pandas as pd
import numpy as np

def practice():

# YOUR TASK: Create this DataFrame
    students = {
        'name': ['John', 'Sarah', 'Mike', 'Emma', 'Alex'],
        'age': [20, 19, 21, 20, 22],
        'grade': ['A', 'B', 'A', 'C', 'B'],
        'city': ['Boston', 'NYC', 'Chicago', 'Boston', 'LA']
    }

# # 1. Create DataFrame from the dictionary
#     df = pd.DataFrame(students)
# # 2. Print the DataFrame
#     print(df)
# # 3. Print the shape (rows, columns)
#     print(df.shape)
# # 4. Print column names
#     print(df.columns)
# # 5. Print data types
#     print(df.dtypes)

#     names = ['Alice', 'Bob', 'Charlie', 'Diana']
#     ages = [25, 30, 35, 28]
#     cities = ['NYC', 'LA', 'Chicago', 'Boston']
#     salaries = [50000, 60000, 70000, 55000]

# # YOUR TASK:
# # 1. Create DataFrame from these lists
# # 2. Set column names: 'name', 'age', 'city', 'salary'
#     df = pd.DataFrame([names,ages,cities,salaries], columns = ['name','age','city','salary'])
# # 3. Display the DataFrame
#     print(df)
# # 4. Display only first 2 rows
#     print(df.loc[[0,2]])

#1.3

# YOUR TASK:
# # 1. Create a DataFrame with at least 5 rows and 3 columns
#     stud = {
#         'name': ['John','Alice','Charlie','Diana','Mike'],
#         'age': [20,19,21,20,22],
#         'grade': ['A','B','C','A','B']
#     }

#     df = pd.DataFrame(stud)
# # 2. Save it as 'sample.csv'
#     df.to_csv('Week 2/Day 4/sample.csv',index=False)
# # 3. Read it back
#     print(pd.read_csv('Week 2/Day 4/sample.csv'))
# # 4. Display the info() of the loaded DataFrame
#     print(df.info())
#     print(df.to_string(index=False))

# Create sample data
    
    # data = {
    # 'product': ['Laptop', 'Mouse', 'Keyboard', 'Monitor', 'Webcam'],
    # 'price': [1200, 25, 75, 300, 150],
    # 'quantity': [5, 50, 30, 10, 20],
    # 'category': ['Electronics', 'Accessories', 'Accessories', 'Electronics', 'Accessories']
    # }
    # df = pd.DataFrame(data)

# # YOUR TASK:
# # 1. Display first 3 rows
#     print(df.head(3))
# # 2. Display last 2 rows
#     print(df.tail(3))
# # 3. Display DataFrame info
#     print(df.info())
# # 4. Display summary statistics
#     print(df.aggregate)
# # 5. Get the shape of DataFrame
#     print(df.shape)

# # YOUR TASK:
# # 1. Select only the 'product' column
#     print(df['product'])
# # 2. Select 'product' and 'price' columns
#     print(df[['product','price']])
# # 3. Select first 2 columns using iloc
#     print(df.iloc[:,0:2])
# # 4. Print data type of each selection
#     print(df.dtypes['product'])


# # YOUR TASK:
# # 1. Filter products with price > 100
#     print(df[df['price']>100])
# # 2. Filter products in 'Electronics' category
#     print(df[df['category'] == 'Electronics'])
# # 3. Filter products with price > 50 AND quantity > 15
#     print(df[(df['price']>50) & (df['quantity']>15)])
# # 4. Filter products that are either 'Laptop' OR 'Monitor'
#     print(df[(df['product'] == 'Laptop') | (df['product'] == 'Monitor')])

# YOUR TASK:
# # 1. Sort by price (ascending)
#     print(df.sort_values(['price'],ascending = True))
# # 2. Sort by price (descending)
#     print(df.sort_values(['price'], ascending = False))
# # 3. Sort by category, then by price
#     print(df.sort_values(['category','price'],ascending = True))
# # 4. Sort by quantity (descending) and display top 3
#     print(df.sort_values(['quantity'],ascending = True).head(3))

    # data = {
    # 'name': ['John', 'Sarah', 'Mike', None, 'Alex'],
    # 'age': [25, None, 30, 28, 35],
    # 'salary': [50000, 60000, None, 55000, None],
    # 'city': ['Boston', 'NYC', 'Chicago', 'Boston', 'LA']
    # }
    # df = pd.DataFrame(data)

# # YOUR TASK:
# # 1. Display the DataFrame
#     print(df)
# # 2. Check for missing values in each column
#     print(df.isnull())
# # 3. Count total missing values per column
#     print(df.isnull().sum())
# # 4. Find which rows have missing values
#     print(df[df.isnull().any(axis=1)])
# # 5. Calculate percentage of missing values per column
#     missing_per = (df.isnull().sum()/len(df))*100
#     print(missing_per)

#     data = {
#     'name': ['John', 'Sarah', 'John', 'Mike', 'Sarah'],
#     'age': [25, 30, 25, 28, 30],
#     'city': ['Boston', 'NYC', 'Boston', 'Chicago', 'NYC']
#     }
#     df = pd.DataFrame(data)

# # YOUR TASK:
# # 1. Display the DataFrame
#     print(df)
# # 2. Check for duplicate rows
#     print(df.duplicated)
# # 3. Count duplicate rows
#     print(df.duplicated().sum())
# # 4. Display only duplicate rows
#     print(df[df.duplicated()])
# # 5. Remove duplicates and display result
#     print(df.drop_duplicates())

    data = {
    'id': ['001', '002', '003', '004'],
    'price': ['100.50', '200.75', '150.25', '300.00'],
    'quantity': ['10', '20', '15', '25'],
    'date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04']
    }
    df = pd.DataFrame(data)

# YOUR TASK:
# 1. Check current data types
    print(df.dtypes)
# 2. Convert 'price' to float
    df['price'] = df['price'].astype(float)
# 3. Convert 'quantity' to int
    df['quantity'] = df['quantity'].astype(int)
# 4. Convert 'date' to datetime
    df['date'] = pd.to_datetime(df['date'])
# 5. Verify the conversions worked
    print(df.dtypes)

practice()