from company_hierarchy_tree import DentWizard
from company_hierarchy_node import *
import pandas as pd

def create_excel(root: CompanyHierarchyNode):
    department_nodes = root.get_departments()
    columns = {
        'Subsidiary': [], 
        'Division': [], 
        'District': [], 
        'Department': [],
        'DVP (Ops)': [], 
        'DVP (Sales)': [], 
        'Regional Admin': [], 
        'DOM': [], 
        'Area Manager': []
    }

    for dept in department_nodes:
        sub = dept.get_subsidiary()
        div = dept.get_division()
        dist = dept.get_district()
        dvp_ops = dept.get_RVP()
        dvp_sales = dept.get_RCDD()
        regional_admin = dept.get_Regional_Admin()
        dom = dept.get_DoM()
        area_manager = dept.get_Area_Manager()

        columns['Subsidiary'].append(sub if sub else '')
        columns['Division'].append(div if div else '')
        columns['District'].append(dist if dist else '')
        columns['Department'].append(dept.name)
        columns['DVP (Ops)'].append(dvp_ops if dvp_ops else '')
        columns['DVP (Sales)'].append(dvp_sales if dvp_sales else '')
        columns['Regional Admin'].append(regional_admin if regional_admin else '')
        columns['DOM'].append(dom if dom else '')
        columns['Area Manager'].append(area_manager if area_manager else '')

    dept_df = pd.DataFrame(columns)
    dept_df['Division Personnel'] = dept_df['DVP (Ops)'].fillna('') + ', ' + dept_df['DVP (Sales)'].fillna('') + ', ' + dept_df['Regional Admin'].fillna('')
    dept_df['Division Personnel'] = dept_df['Division Personnel'].str.strip(', ')
    
    dept_df_revised = dept_df[
        ['Subsidiary', 'Division', 'District', 'Department', 'Division Personnel', 'DOM', 'Area Manager']
    ]

    dept_df_revised.to_excel('Dept_test.xlsx')
    return dept_df_revised

def main():
    create_excel(DentWizard)

if __name__ == "__main__":
    main()
