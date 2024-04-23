from connection_test import *

def filter_dataframe(df):
    column_name = input("Enter the column name to filter by: ")
    filter_value = input(f"Enter the value for {column_name}: ")
    filtered_df = df[df[column_name] == filter_value]
    print(filtered_df)

def summarize_data(df):
    column_name = input("Enter the column name to summarize: ")
    print(df[column_name].describe())

def set_current_db():
    db_name = input("Enter database name: ")
    execute_session_command(f"USE DATABASE {db_name};")

def set_current_wh():
    wh_name = input("Enter warehouse name: ")
    execute_session_command(f"USE WAREHOUSE {wh_name};")

def select_from_view():
    database_name = input("Enter the database name (or leave blank to use current): ")
    schema_name = input("Enter the schema name (or leave blank to use current): ")
    
    if database_name:
        execute_session_command(f"USE DATABASE {database_name};")
    if schema_name:
        execute_session_command(f"USE SCHEMA {schema_name};")
    
    view_name = input("Enter the name of the view: ")
    columns = input("Enter columns to select (or '*' for all): ").strip()
    if not columns:
        columns = '*'
    
    try:
        row_limit = int(input("Enter the number of rows to fetch (0 for no limit): "))
    except ValueError:
        row_limit = 0  # Default to no limit if input is not a valid integer
    
    query = f'SELECT {columns} FROM "{view_name}"'
    if row_limit > 0:
        query += f"LIMIT {row_limit}"

    df = execute_query_and_load_data(query)
    if not df.empty:
        return(df)
    else:
        print("No data found or an error occurred.")


#To group by district we can use the df.agg method then input the specific types for each column. 
#e.g,: grouped_by_district = df.groupby('DEPARTMENT_DISTRICT_NAME').agg({'Total Expense' : 'sum', 'Total Revenue':'sum', 'Date': 'first'})
#grouped_by_acc_district = df.groupby(['DEPARTMENT_DISTRICT_NAME', 'Account Name']).agg({'Total Expense' : 'sum', 'Total Revenue':'sum', 'Date': 'first', 'ACCOUNT_NUMBER':'first}) THIS IS THE ONE
        
#need to make sure non-numeric columns are not aggregated by 'sum
