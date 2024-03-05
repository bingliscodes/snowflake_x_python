import snowflake.connector
from dotenv import load_dotenv
import os
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
    print("3. Exit")

def execute_query(query):
    try:
        cur.execute(query)
        # Fetch and print the results for demonstration purposes
        for row in cur.fetchall():
            print(row)
    except Exception as e:
        print(f"An error occurred: {e}")

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
            print("Exiting...")
            break
        else:
            print("Invalid choice, please try again.")

    # Clean up before exiting
    cur.close()
    connection.close()

if __name__ == "__main__":
    main()