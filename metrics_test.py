from account_organization import *
from connection_test import *
from collections import defaultdict

#Let's use a dictionary (account_dict) to include all the accounts in each subcategory of the hierarchy


#cur is the cursor object from connection test

#Step 1: Query all the revenue data

actuals_query = """
SELECT * FROM DEPT_FINANCE.PUBLIC.BENS_PL_ACTUALS
"""

budget_query = """
SELECT * FROM DEPT_FINANCE.PUBLIC.BENS_PL_BUDGET
"""

#actuals_df = execute_query_and_load_data(actuals_query)

### ACTUALS VALIDATION ###
# actuals_df = execute_query_and_load_data(actuals_query)
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
 

"""
For Actuals (2024-01-01)
Right:
    Other Revenue
    Gross Revenue 
    Gross Service Revenue
    Discounts 
    Net Revenue 
    Tech Wages
    Sub-Let Labor
    Tech Tools & Supplies
    Tech T&E
    Tech Cell Phones
    Tech Other
    SG&A Wages
    SG&A Benefits and Taxes
    SG&A T&E
    SG&A Cellphone
    SG&A Employee Relations
    SG&A Postage and Supplies (SG&A Supplies)
    SG&A Facility
    SG&A Adv/Mkt (SG&A Advertising & Marketing)
    SG&A Other
    Tech Benefits & Taxes
    Tech Vehichle Expense
    Total Tech Expenses (Tech Cost of Sales)
    Gross Margin (Gross Profit)
    SG&A Vehichle Expense
    Total SG&A
    EBITDA

Tech Vehicle is off by $524 in Jan 2024, but correct for Feb 2024
SG&A ADV/MKT is off by ~500 in Jan 2024, but correct for Feb 2024
For Budget (2024-01-01)

Right: (2024-01-01)
Other Revenue
F&I Revenue
Discounts
Tech Wages
Tech Benefits
Sublet Labor
Tech Tools & Supplies
Tech Vehicle
Tech Cell
Tech Other
Total Tech Expense
SG&A Wages
SG&A B&T
SG&A Vehicle
SG&A Travel and Entertainment
SG&A Cell
SG&A Employee Relations
SG&A Supplies
SG&A Facility
SG&A Adv/Mkt
SG&A Other
Total SG&A


Wrong: (2024-01-01)
Gross Service Revenue
Gross Margin (Gross Profit)
Net Revenue

#Tech LSR is 23038121 (confirmed)
#Tech Other is 5976585 (confirmed)
#Tech total should be 29014706 (confirmed)
#Added 3005500
"""