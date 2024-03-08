import snowflake.connector
from dotenv import load_dotenv
import os
import pandas as pd
from data_operations import *
from account_organization import *
import IPython
load_dotenv()

connection_params = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('DW_PASSWORD'),
    'account': os.getenv('DW_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    #'schema': os.getenv('SNOWFLAKE_SCHEMA'),
}
# Establishing connection
connection = snowflake.connector.connect(
    user=connection_params['user'],
    password=connection_params['password'],
    account=connection_params['account'],
    warehouse=connection_params['warehouse'],
    database=connection_params['database'],
    #schema=connection_params['schema'],
    authenticator='snowflake',
)


# Creating a cursor object
cur = connection.cursor()

def main_menu():
    print("\nWelcome to the Snowflake Interactive Menu")
    print("1. Execute Query and Load Data")
    print("2. Filter Data")
    print("3. Summarize Data")
    print("4. Select Data from a View")
    print("5. Set Current Database")
    print("6. Set Current Warehouse")
    print("7. Exit")

# For data retrieval operations
def execute_query_and_load_data(query):
    try:
        cur.execute(query)
        df = cur.fetch_pandas_all()
        return df
    except Exception as e:
        print(f"An error occurred: {e}")
        return pd.DataFrame()  # Return an empty DataFrame in case of an error

# For context-setting operations
def execute_session_command(command):
    try:
        cur.execute(command)
        print("Session command executed successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

df = None
def main():
    global df
    df = pd.DataFrame()

    while True:
        main_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            query = input("Enter your SQL query: ")
            df = execute_query_and_load_data(query)
        elif choice == "2" and not df.empty:
            filter_dataframe(df)
        elif choice == "3" and not df.empty:
            summarize_data(df)
        elif choice == "4":
            df = select_from_view()
        elif choice == "5":
            set_current_db()
        elif choice == "6":
            set_current_wh()
        elif choice == "7":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

    # Clean up before exiting
    cur.close()
    connection.close()

if __name__ == "__main__":
    main()
    if df is not None:
        print("DataFrame is now accessible.")
    IPython.embed()

