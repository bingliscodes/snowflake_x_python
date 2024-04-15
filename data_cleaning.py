from connection_test import connection, connection_params, execute_query_and_load_data
from sql_queries import *
from hierarchy_tree import *
from datetime import date
from collections import defaultdict
import pandas as pd

tabs = defaultdict(pd.DataFrame)
cur = connection.cursor()

#Step 1: Acquire data
master_lookup_tabs = [
    ["Items", Items_query],
    ["Employees", Employees_query],
    ["Consignors", Consignors_query],
    ["Partners", Partners_query],
    ["Departments", Departments_query],
    ["Customers", Customers_query]
]

ret = []
for tabName, queryName in master_lookup_tabs:
    tabs[tabName] = execute_query_and_load_data(queryName)

print(tabs)


# #Step 2: Order columns 
# order_dict = {
#     "Customer Company Name": 1,
#     "Document Number": 2,
#     "Service Calendar Date": 3,
#     "Product Line": 4,
#     "Key Item Combined": 5,
#     "Invoice Quantity": 6,
#     "VIN (Transactions)": 7,
#     "Invoice Net Amount": 8,
#     "Level 2 Parent Customer Company Name": 9,
#     "RO": 10,
#     "Stock Number": 11,
#     "Vehicle Year": 12,
#     "Vehicle Make": 13,
#     "Vehicle Model": 14,
#     "Key Category 1": 15,
#     "Key Type 2": 16,
#     "Price Level Type Name": 17,
#     "KMX Key #": 18,
#     "Calendar Created Date": 19,
#     "Invoice Description": 20,
#     "Customer Category": 21
# }

# ordered_columns = sorted(order_dict, key=order_dict.get)


# Append any other columns not specified in the dictionary, maintaining their original order
#ordered_columns += [col for col in df.columns if col not in ordered_columns]

#Step 3: save as csv and email
file_name = "Master Lookup - " + date.today().strftime("%m%y") + ".xlsx"

with pd.ExcelWriter(file_name) as writer:
    for tab in tabs:
        tabs[tab].to_excel(writer, sheet_name=tab, index=False)



#df.to_csv(path_or_buf= save_name)

cur.close()
connection.close()

"""
"""