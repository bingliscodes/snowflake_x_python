import snowflake.connector
from dotenv import load_dotenv
import os
#import logging

#clogging.basicConfig(level=logging.DEBUG)

load_dotenv()

connection_params = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA'),
    'login_timeout': 10,
    'network_timeout': 15,
}
# Establishing connection
print("establishing connection...")
connection = snowflake.connector.connect(
    user=connection_params['user'],
    password=connection_params['password'],
    account=connection_params['account'],
    warehouse=connection_params['warehouse'],
    database=connection_params['database'],
    schema=connection_params['schema'],
    login_timeout=connection_params['login_timeout'], 
    network_timeout=connection_params['network_timeout'],
    authenticator='snowflake',
)

print("connected")

# Creating a cursor object
cur = connection.cursor()

try:
    print("entering try")
    # Executing a query
    cur.execute("SELECT CURRENT_DATE;")

    # Fetching one result
    one_row = cur.fetchone()
    print("Current Date:", one_row)
finally:
    # Closing the cursor and connection
    cur.close()
    connection.close()

