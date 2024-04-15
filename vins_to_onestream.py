from connection_test import connection, connection_params, execute_query_and_load_data
from sql_queries import VINs_query
from hierarchy_tree import *
from datetime import date
from collections import defaultdict
import pandas as pd

vins_df = execute_query_and_load_data(VINs_query)

vins_df['New Name'] = vins_df['Account Number'].astype(str) + ' - ' + vins_df['Account Name'] + '- Vin Ct'

vins_df_to_csv = vins_df[['New Name', 'Sales Channel Name', 'Department/Zone', 'VIN Count']]

vins_df_to_csv.to_csv('VINS_to_Onestream_test.csv')