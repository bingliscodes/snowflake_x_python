#company_hierarchy_tree.py
from syspath import *
from collections import defaultdict
from sql_queries import Departments_query
from company_hierarchy_node import *
import pandas as pd
from connection_test import connection, connection_params, execute_query_and_load_data


#dept_df = execute_query_and_load_data(Departments_query)
#remove inactives
dept_df = pd.read_excel(r'C:\Users\BInglis\Code\Snowflake_Py_Project\Project\Company_Hierarchy\Dept_csv.xlsx') #temporary solution until we get subsidiaries
boolean_mask = dept_df['Inactive'] == 'Yes'
dept_df = dept_df[~boolean_mask]

# Initialize default dictionaries for each level of the hierarchy
subsidiary_dict = defaultdict(lambda: None)
division_dict = defaultdict(lambda: None)
district_dict = defaultdict(lambda: None)
department_dict = defaultdict(lambda: None)

DentWizard = CompanyHierarchyNode("Dent Wizard", "Company")
# Create or get nodes for each level, ensuring no duplicates
for _, row in dept_df.iterrows():
    # Unpack row values once
    sub, div, dist, dept = row['Subsidiary'], row['Division'], row['District'], row['Department']

    # Get or create subsidiary node
    sub_node = subsidiary_dict[sub]
    if sub_node is None:
        sub_node = CompanyHierarchyNode(sub, 'Subsidiary', parent=DentWizard)
        DentWizard.add_child(sub_node)
        subsidiary_dict[sub] = sub_node

    # Get or create division node
    div_key = (sub, div)
    div_node = division_dict[div_key]
    if div_node is None:
        div_node = CompanyHierarchyNode(div, 'Division', parent=sub_node)
        sub_node.add_child(div_node)
        division_dict[div_key] = div_node

    # Get or create district node
    dist_key = (sub, div, dist)
    dist_node = district_dict[dist_key]
    if dist_node is None:
        dist_node = CompanyHierarchyNode(dist, 'District', parent=div_node)
        div_node.add_child(dist_node)
        district_dict[dist_key] = dist_node

    # Get or create department node
    dept_key = (sub, div, dist, dept)
    dept_node = department_dict[dept_key]
    if dept_node is None:
        dept_node = CompanyHierarchyNode(dept, 'Department', parent=dist_node)
        dist_node.add_child(dept_node)
        department_dict[dept_key] = dept_node

    #assigning roles
    if 'RVP' in row and row['RVP']:
        div_node.assign_role('DVP (Ops)', row['RVP'])

    if 'RCDD' in row and row['RCDD']:
        div_node.assign_role('DVP (Sales)', row['RCDD'])
    
    if 'Regional Admin' in row and row['Regional Admin']:
        div_node.assign_role('Regional Admin', row['Regional Admin'])

    if 'DM/MM Name' in row and row['DM/MM Name']:
        dist_node.assign_role('DOM', row['DM/MM Name'])

    if 'Area Manager' in row and row['Area Manager']:
        dept_node.assign_role('Area Manager', row['Area Manager'])

DentWizard.display_hierarchy()