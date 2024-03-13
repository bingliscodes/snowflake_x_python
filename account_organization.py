#this script is to help organize the df rows into the appropriate lowest level of the hierarchy by account number.
from hierarchy_tree import *
from collections import defaultdict
import pandas as pd
import csv

#this function goes through the dataframe and adds the label for the appropriate lowest level account category for each row.


def addLabels(df):
    df['Account Label'] = df.apply(
        lambda x: DentWizard.find_category_by_account(x['ACCOUNT_NUMBER']),
        axis= 1
    )
    return df

def flatten_hierarchy(node, path=None, parent_name=""):
    if path is None:
        path = []
    # Update the path for the current node
    current_path = path + [node.name]
    rows = []
    if hasattr(node, 'account_numbers'):
        for account_number in node.account_numbers:
            rows.append({
                'Account Number': str(account_number),
                'Category Name': node.name,
                'Parent Category': parent_name,  # Include the parent category
                'Path': " > ".join(current_path)
            })
    else:
        for child in node.children:
            # Pass the current node's name as the parent name for its children
            rows.extend(flatten_hierarchy(child, current_path, node.name))
    return rows


def export_to_csv(nodes, file_name='hierarchy.csv'):
    fieldnames = ['Account Number', 'Category Name', 'Parent Category', 'Path']
    with open(file_name, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for node in nodes:
            writer.writerows(flatten_hierarchy(node))



#export_to_csv([DentWizard])
