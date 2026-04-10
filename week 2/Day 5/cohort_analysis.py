import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pylab as plt

def cohort():

    filename = ("Week 2/Day 5/customer cohort files/customer_data.csv")
    fn = ("Week 2/Day 5/customer cohort files/cohort_statistics.xlsx")

    def get_data(filename):
        try:
            df = pd.read_csv(filename, sep = ',', na_values = ['nan','NaN','N/A', 'NA'], header = 0)
            df.replace(['NaN','nan','NAN','None','N/A','NA'], np.nan)
            df['order_date'] = pd.to_datetime(df['order_date'])
            return df

        except Exception as e:
            print(f"Unable to get data: {e}")

    def load_data(df):
        try:
            print("Data from file")
            df = df.sort_values('order_date', ascending = True, ignore_index = True )
            print(df)
            return df

        except Exception as e:
            print(f"Unable to load data: {e}")

    def create_cohorts(df):
        try:
            df['first_purchase_date'] = df.groupby('customer_id')['order_date'].transform('min')
            df['cohort_month'] = df['first_purchase_date'].dt.to_period('M')
            df['order_month'] = df['order_date'].dt.to_period('M')
            df['months_since_first_purchase'] = (df['order_month']-df['cohort_month']).apply(lambda x:x.n)
            print("Months since first purchase:")
            print(df)
            return df

        except Exception as e:
            print(f"Cohort creation failed: {e}")

    def calculate_retention(df):
        try:
           piv =  df.pivot_table(index = 'cohort_month', columns = 'months_since_first_purchase', values = 'customer_id', aggfunc = 'nunique')
           piv_size = piv.iloc[:,0]
           retention_matrix = piv.divide(piv_size, axis = 0)
           retention_matrix = (retention_matrix*100).round(2)
           print(retention_matrix)
           return retention_matrix

        except Exception as e:
            print(f"Retention calculation failed: {e}")

    def cohort_revenue_analysis(df):
        try:
            print(df)
            df['revenue'] = df.groupby('customer_id')['order_value'].transform('sum')
            df['average'] = df.groupby('customer_id')['order_value'].transform('mean').round(2)
            df['orders'] = df.groupby('customer_id')['order_value'].transform('count')
            print("Updated Data:")
            print(df)
            print("")
            maximum_sales = df.sort_values('revenue', ascending = False).max()
            print("Customer with High sales Value: ")
            print("")
            print(maximum_sales)
            return df

        except Exception as e:
            print(f"revenue analysis failed: {e}")

    def life_time_analysis(df):
        try:
            df['LTV_per_cohort'] = df.groupby(['months_since_first_purchase', 'cohort_month'])['order_value'].transform('mean').round(2)
            ltv_piv = df.pivot_table(index = 'cohort_month', columns = 'months_since_first_purchase' , values = 'LTV_per_cohort').cumsum(axis=1)
            growth_rate = ltv_piv.pct_change(axis = 1).mean()
            pred_df = ltv_piv.copy()

            for col in range(1, len(pred_df.columns)):
                multiplier = 1 + growth_rate.iloc[col]
                pred_df.iloc[:,col] = pred_df.iloc[:,col].fillna(pred_df.iloc[:,col-1]*multiplier)
                pred_df = pred_df.round(2)

            ltv_piv.T.plot(fig = (10,5), marker = 'o')
            plt.title('LIFE TIME VALUE CURVE')
            plt.xlabel('Month Since First Purchase')
            plt.ylabel('Cumulative Revenue per Customer')
            plt.legend(title='Cohort', bbox_to_anchor=(1.05, 1), loc='upper left')
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.savefig('Week 2/Day 5/customer cohort files/Life_time_value.png')
            plt.show()

            pred_df.T.plot(fig = (10,5), marker ='o')
            plt.title('PREDICTION CURVE')
            plt.xlabel('Month Since First Purchase')
            plt.ylabel('Predicted Cumulative Revenue per Customer')
            plt.legend(title = 'Cohort', bbox_to_anchor = (1.05, 1), loc = 'upper left')
            plt.grid(True, linestyle = '--', alpha = 0.6)
            plt.savefig('Week 2/Day 5/customer cohort files/prediction.png')
            plt.show()

            print("Life time analysis pivot table:")
            print(ltv_piv)
            print("Predicted future costs: ")
            print(pred_df)

            return ltv_piv, pred_df

        except Exception as e:
            print(f"LTV Analysis failed: {e}")

    def visualise_cohorts(rm):
        try:
            plt.figure(figsize = (12,8))
            plt.title('Retention Curve', fontsize = 16)
            sns.heatmap(rm, fmt = '.2f', cmap = 'YlGnBu', annot = True, linewidths = .5 )
            plt.xlabel('month_since_first_purchase')
            plt.ylabel('cohort_month')
            plt.savefig('Week 2/Day 5/customer cohort files/Retention_graph.png')
            plt.show()

        except Exception as e:
            print(f"Cohort Visualisation failed: {e}")

    def generate_cohort_report(dt,df,rm,ltv,pred,fn):
        try:
            with pd.ExcelWriter(fn, engine = 'xlsxwriter') as writer:
                dt.to_excel(writer, sheet_name = 'Raw Data', index = False)
                df.to_excel(writer, sheet_name = 'Cohort Revenue Analysis', index = False)
                rm.to_excel(writer, sheet_name = 'Retention Matrix', index = True)
                ltv.to_excel(writer, sheet_name = 'Life time Value', index = True)
                pred.to_excel(writer, sheet_name = 'Future prediction', index = True)

                workbook = writer.book
                retention_sheet = writer.sheets['Retention Matrix']
                life_time_value = writer.sheets['Life time Value']
                future_prediction = writer.sheets['Future prediction']

                retention_sheet.conditional_format(1, 1, len(rm), len(rm.columns),
                                            {'type': '2_color_scale',
                                             'min_color': "#FF7C80",
                                             'max_color': "#C6EFCE"})
                try:
                    retention_sheet.insert_image('J2', 'Week 2/Day 5/customer cohort files/Retention_graph.png', 
                                           {'x_scale': 0.5, 'y_scale': 0.5})
                    life_time_value.insert_image('J2', 'Week 2/Day 5/customer cohort files/Life_time_value.png',
                                           {'x_scale': 0.5, 'y_scale': 0.5})
                    future_prediction.insert_image('J2', 'Week 2/Day 5/customer cohort files/prediction.png',
                                           {'x_scale': 0.5, 'y_scale':0.5})
                    
                except:
                    print("Note: Retention_graph.png not found. Run choice 6 first to include the image.")

            print(f"Statistics successfully saved to path: {fn}")

        except Exception as e:
            print(f"Unable to generate statistics report: {e}")

    data = get_data(filename)
    dt = None
    rm = None
    ltv = None
    pred = None

    if data is None:
        print("Unable to retreive data")
        return
    
    while True:
        print("COHORT ANALYSIS DASHBOARD")
        print("1. Load raw data")
        print("2. Create cohorts")
        print("3. Calculate retention")
        print("4. Cohort Revenue Analysis")
        print("5. Lifetime value and future predictions")
        print("6. Visualise Cohorts")
        print("7. Generate Report")
        print("8. Exit")

        ch = input("Please enter a choice from 1-8: ")

        if ch == "1":
            dt = load_data(data)
        elif ch == "2":
            data = create_cohorts(dt)
        elif ch == "3":
            rm = calculate_retention(data)
        elif ch == "4":
            data = cohort_revenue_analysis(data)
        elif ch == "5":
            ltv, pred = life_time_analysis(data)
        elif ch == "6":
            visualise_cohorts(rm)
        elif ch == "7":
            generate_cohort_report(dt,data,rm,ltv,pred,fn)
        elif ch == "8":
            print("Quitting...")
            break
        else:
            print("Invalid choice")
        
cohort()