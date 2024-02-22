from snowflake.snowpark import Session #pip install snowflake-snowpark-python
from snowflake.core import Root #pip install snowflake -U
from dotenv import load_dotenv
import os
import pyarrow as pa #pip install pyarrow
#pa.set_timezone_db_path("custom_path") #if using windows, uncomment this. See PyArrow documentation for installation
root = Root(session)
load_dotenv()

conn_params = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('SNOWFLAKE_PASSWORD'),
    'account': os.getenv('SNOWFLAKE_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    'schema': os.getenv('SNOWFLAKE_SCHEMA'),
}

new_session = Session.builder.configs(conn_params).create()

#close the session when finished
new_session.close()