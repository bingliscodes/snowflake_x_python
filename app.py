from snowflake.core import Root
from snowflake.core.task import Task
from snowflake.snowpark import Session

session = Session.builder.config("connection_name", "myconnection").create()
root = Root(session)

tasks = root.databases["mydb"].schemas["myschema"].tasks
task_res = tasks['my_task']

task_res.execute()