import snowflake.connector
from snowflake.snowpark import Session #pip install snowflake-snowpark-python
from snowflake.core import Root #pip install snowflake -U
from dotenv import load_dotenv
import os
import pyarrow as pa #pip install pyarrow
#pa.set_timezone_db_path("custom_path") #if using windows, uncomment this. See PyArrow documentation for installation
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
    sql = "SELECT * FROM SAMPLE_PL_NE"
    cur.execute(sql)

    df = cur.fetch_pandas_all()
    print(df)
finally:
    # Closing the cursor and connection
    cur.close()
    connection.close()

