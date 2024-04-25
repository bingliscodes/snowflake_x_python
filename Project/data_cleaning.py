from connection_test import connection, connection_params, execute_query_and_load_data
from Project.sql_queries import *
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
    ["Discounts", Discounts_query]
]

#Step 2: Load data into dataframes
for tabName, queryName in master_lookup_tabs:
    tabs[tabName] = execute_query_and_load_data(queryName)


#Step 3: save as xlsx file and email
file_name = "Master Lookup - " + date.today().strftime("%m%y") + ".xlsx"

with pd.ExcelWriter(file_name) as writer:
    for tab in tabs:
        tabs[tab].to_excel(writer, sheet_name=tab, index=False)

cur.close()
connection.close()