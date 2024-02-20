import snowflake.connector
from dotenv import load_dotenv
import os

load_dotenv()

connection_params = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA'),
}
# Establishing connection
connection = snowflake.connector.connect(**connection_params)

# Creating a cursor object
cur = connection.cursor()

try:
    # Executing a query
    cur.execute("SELECT CURRENT_VERSION()")

    # Fetching one result
    one_row = cur.fetchone()
    print(one_row)
finally:
    # Closing the cursor and connection
    cur.close()
    connection.close()

