from account_organization import *
from connection_test import *
from collections import defaultdict

#Let's use a dictionary (account_dict) to include all the accounts in each subcategory of the hierarchy


#cur is the cursor object from connection test

#Step 1: Query all the revenue data

actuals_query = """
SELECT * FROM DEPT_FINANCE.PUBLIC.BENS_PL_ACTUALS
WHERE "Account Period Name" = 'Jan 2023'
"""

budget_query = """
SELECT * FROM DEPT_FINANCE.PUBLIC.BENS_PL_BUDGET
WHERE "Account Period Name" = 'Jan 2024';
"""

actuals_df = execute_query_and_load_data(actuals_query)
   

### ACTUALS VALIDATION ###
# actuals_df = execute_query_and_load_data(actuals_query)
# for metric in account_dict:
#     total = actuals_df[actuals_df['Account Number'].isin(account_dict[metric])]
#     print(metric, "total is: ", total['Net Sign Rev'].sum())


### BUDGET VALIDATION ###
budget_df = execute_query_and_load_data(budget_query)
budget_df.loc[budget_df['Account Type'] == 'Expense', 'Budget Amount USD'] *= -1
budget_df.loc[budget_df['Account Number'] == '3032100', 'Budget Amount USD'] *= -1

for metric in account_dict:
    total = budget_df[budget_df['Account Number'].isin(account_dict[metric])]
    print(metric, "total is: ", total['Budget Amount USD'].sum())
 

"""
For Actuals
Right:
    Other Revenue is correct
    Gross Revenue is correct
    Gross Service Revenue is correct
    Discounts is correct
    Net Revenue is correct
    Tech Wages is correct
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

For Budget (2023-01-01)

Right:
Gross Service Revenue
Other Revenue
F&I Revenue
Net Revenue
Tech Wages
Tech Benefits & Taxes
Sublet Labor
Tech Tools & Supplies
Tech Vehicle
Tech T&E
Tech Cell Phones
Tech Other
Total Tech Expenses (Tech Cost of Sales)
SG&A Wages
SG&A Benefits
SG&A Vehicle
SG&A Cell Phones
SG&A Employee Relations
SG&A Postage and Supplies (SG&A Supplies)
SG&A Facility
SG&A Adv/Mkt (SG&A Advertising & Marketing)
SG&A Other
Total SG&A
Discounts (-3274894 vs. -3273390)
Gross Margin (Gross Profit)
EBITDA


Wrong: (2024-01-01)
"""
#TODO: Try multiplying "expense type" account by -1 