from connection_test import connection, connection_params, execute_query_and_load_data
from sql_queries import *
from hierarchy_tree import *


cur = connection.cursor()

df = execute_query_and_load_data(all_query)
df.to_csv('data_dump.csv')

cur.close()
connection.close()