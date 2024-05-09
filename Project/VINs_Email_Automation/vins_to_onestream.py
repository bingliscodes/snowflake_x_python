from syspath import *
from connection_test import connection, connection_params, execute_query_and_load_data
from sql_queries import VINs_query
from hierarchy_tree import *
from datetime import date
from collections import defaultdict


vins_df = execute_query_and_load_data(VINs_query)

vins_df['New Name'] = 'DWVIN_' + vins_df['Account Number'].astype(str)

vins_df_to_csv = vins_df[['New Name', 'Sales Channel Name', 'Department/Zone', 'VIN Count', 'Subsidiary']]

vins_df_to_csv.to_csv('VINS_to_Onestream_0424.csv')

