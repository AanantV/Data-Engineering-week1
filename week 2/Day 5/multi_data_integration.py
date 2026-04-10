import pandas as pd
import numpy as np

def multi_src():

    emp = "Week 2/Day 5/Multi source files/employees.csv"
    sal = "Week 2/Day 5/Multi source files/salaries.csv"
    perf = "Week 2/Day 5/Multi source files/performance.csv"
    dept = "Week 2/Day 5/Multi source files/departments.csv"

    def load_multiple_data():
        try:
            employee = pd.read_csv(emp, sep = ',', header = 0, na_values = ['NaN', 'nan', 'N/A', 'NA'])
            employee.replace(['NaN', 'NAN', 'None', 'none', 'NA', 'N/A', 'nan'], np.nan)
            salary = pd.read_csv(sal, sep = ',', header = 0, na_values = ['NaN', 'nan', 'N/A', 'NA'])
            salary.replace(['NaN', 'NAN', 'None', 'none', 'NA', 'N/A', 'nan'], np.nan)
            performance = pd.read_csv(perf, sep = ',', header = 0, na_values = ['NaN', 'nan', 'N/A', 'NA'])
            performance.replace(['NaN', 'NAN', 'None', 'none', 'NA', 'N/A', 'nan'], np.nan)
            department = pd.read_csv(dept, sep = ',', header = 0, na_values = ['NaN', 'nan', 'N/A', 'NA'])
            department.replace(['NaN', 'NAN', 'None', 'none', 'NA', 'N/A', 'nan'], np.nan)

            dept_with_no_id = employee['dept_id']
            empty_dept = department[~department['dept_id'].isin(dept_with_no_id)]

            df = pd.merge(employee, department, on='dept_id', how= 'outer')
            df = pd.merge(df, performance, on='emp_id', how = 'outer')
            df = pd.merge(df, salary, on='emp_id', how='outer')

            df['emp_id'] = df['emp_id'].astype('Int64')
            df['hire_date'] = pd.to_datetime(df['hire_date'])
            df['year'] = pd.to_datetime(df['year'], format = '%Y').dt.to_period('Y')

            df.replace(['NaN', 'NAN', 'None', 'none', 'NA', 'N/A', 'nan', 'NaT', 'nat', 'NAT','<NA>'], np.nan)
            print(df)
            return df, empty_dept

        except Exception as e:
            print(f'Unable to load data: {e}')

    def validate_data(df, emp):
        try:
            print("Empty departments:")
            print(emp)
            print("Number of null values in the dataframe(columnwise):\n")
            print(df.isna().sum())
            print(f"\nNumber of duplicates in the dataframe: {df.duplicated().sum()}")
            updated_df = df.dropna()
            updated_df = updated_df.drop_duplicates()
            print("\nUpdated Dataframe:")
            print(updated_df)
            print("Complexities after removing duplicates and nulls:")
            print("\nNull Report:")
            print(updated_df.isna().sum())
            print(f"\nNumber of duplicates in the dataframe: {updated_df.duplicated().sum()}")
            return updated_df

        except Exception as e:
            print(f"data validation failed: {e}")

    def merge_all_data(df):
        try:
            print("Consolidated Dataframe:")
            print(df)
            df['compensation'] = df['base_salary'] + df['bonus']
            df['YoE'] = df.groupby('emp_id')['year'].transform('count')
            df['dept_size'] = df.groupby(['dept_id','year'])['emp_id'].transform('count')
            print("Updates made in Data: Added compensation, YoE, dept_size columns\n")
            print(df)
            return df

        except Exception as e:
            print(f"Data merge failed: {e}")

    def cross_tabulate(df):
        try:


        except Exception as e:
            print(f"Cross tabulation failed: {e}")

    data, empty_dept = load_multiple_data()

    if data is not None:
        data = validate_data(data, empty_dept)
        merge_all_data(data)


multi_src()