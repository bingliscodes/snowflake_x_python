import snowflake.connector
from dotenv import load_dotenv
import os
import pandas as pd
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
    print("1. Show Databases")
    print("2. Run Custom Query")
    print("3. Set Current Database")
    print("4. Set Current Warehouse")
    print("5. Exit")

def set_current_db():
    db_name = input("Enter database name: ")
    execute_query(f"USE DATABASE {db_name};")

def set_current_wh():
    wh_name = input("Enter warehouse name: ")
    execute_query(f"USE WAREHOUSE {wh_name};")

def execute_query(query):
    try:
        cur.execute(query)
        if cur.rowcount > 0:
            try:
                df = cur.fetch_pandas_all()
                print(df)
            except Exception as e:
                print("Query executed successfully, but no data was returned for DataFrame. {e}")
        else:
            print("Query executed successfully, but it does not return a result set.")
    except Exception as e:
        print(f"An error occurred {e}")

def run_custom_query():
    query = input("Enter your SQL query: ")
    execute_query(query)

def main():
    while True:
        main_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            execute_query("SHOW DATABASES")
        elif choice == "2":
            run_custom_query()
        elif choice == "3":
            set_current_db()
        elif choice == "4":
            set_current_wh()
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

    # Clean up before exiting
    cur.close()
    connection.close()

if __name__ == "__main__":
    main()