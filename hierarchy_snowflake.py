import snowflake.connector
from connection_test import connection_params  # Assuming connection parameters are defined in connection_test.py
from hierarchy_tree import DentWizard  # Assuming your hierarchy tree is defined in hierarchy_tree.py

# Function to create tables in Snowflake if they don't already exist
def create_tables(cursor):
    # Check if the AccountHierarchy table exists
    cursor.execute("SHOW TABLES LIKE 'ACCOUNTHIERARCHY'")
    if not cursor.fetchone():
        # Create the AccountHierarchy table
        create_account_hierarchy_table = """
        CREATE TABLE AccountHierarchy (
            id INTEGER AUTOINCREMENT PRIMARY KEY,
            name VARCHAR(255)
        );
        """
        cursor.execute(create_account_hierarchy_table)

    # Check if the AccountHierarchyRelationships table exists
    cursor.execute("SHOW TABLES LIKE 'ACCOUNTHIERARCHYRELATIONSHIPS'")
    if not cursor.fetchone():
        # Create the AccountHierarchyRelationships table
        create_relationships_table = """
        CREATE TABLE AccountHierarchyRelationships (
            parent_id INTEGER,
            child_id INTEGER,
            FOREIGN KEY (parent_id) REFERENCES AccountHierarchy(id),
            FOREIGN KEY (child_id) REFERENCES AccountHierarchy(id)
        );
        """
        cursor.execute(create_relationships_table)

# Function to recursively insert nodes and their relationships into Snowflake
def insert_node(cursor, parent_id, node):
    cursor.execute(
        "INSERT INTO AccountHierarchy (name) VALUES (%s)", 
        (node.name,)
    )
    
    # Fetch the maximum ID from the AccountHierarchy table
    cursor.execute("SELECT MAX(id) FROM AccountHierarchy")
    node_id = cursor.fetchone()[0]
    
    cursor.execute(
        "INSERT INTO AccountHierarchyRelationships (parent_id, child_id) VALUES (%s, %s)", 
        (parent_id, node_id)
    )
    
    for child in node.children:
        insert_node(cursor, node_id, child)




try:
    connection = snowflake.connector.connect(
        user=connection_params['user'],
        password=connection_params['password'],
        account=connection_params['account'],
        warehouse='ANALYTICS_WH',
        database='DEPT_FINANCE',
        schema='PUBLIC',
        authenticator='snowflake'
    )

    # Creating a cursor object
    cursor = connection.cursor()

    # Creating tables
    create_tables(cursor)

    # Starting a transaction
    connection.autocommit(False)

    # Recursively insert nodes and relationships into Snowflake
    for child in DentWizard.children:
        insert_node(cursor, None, child)

    # Committing the transaction
    connection.commit()
    print("Data inserted successfully.")
finally:
    # Closing the cursor and connection
    cursor.close()
    connection.close()
