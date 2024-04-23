#metrics_test.py
from account_organization import *
from connection_test import *
from Project.sql_queries import *


### ACTUALS VALIDATION ###
actuals_df = execute_query_and_load_data(actuals_query)
# for metric in account_dict:
#     total = actuals_df[actuals_df['Account Number'].isin(account_dict[metric])]
#     print(metric, "total is: ", total['Net Sign Rev'].sum())

expense_accounts = ['Expense', 'Cost of Goods Sold', 'Other Expense']
### BUDGET VALIDATION ###
#budget_df = execute_query_and_load_data(budget_query)
#this works for 2023-01-01 and 2024-01-01
#budget_df.loc[budget_df['Account Type'].isin(expense_accounts), 'Budget Amount USD'] *= -1

# for metric in account_dict:
#     total = budget_df[budget_df['Account Number'].isin(account_dict[metric])]
#     print(metric, "total is: ", total[metric].sum())
 
def get_actuals_and_budgets():
    actuals_df = execute_query_and_load_data(actuals_query)
    budget_df = execute_query_and_load_data(budget_query)
    # Perform any necessary initial processing here
    return actuals_df, budget_df
