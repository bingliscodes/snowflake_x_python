#this script is to help organize the df rows into the appropriate lowest level of the hierarchy by account number.
from hierarchy_tree import *
from collections import defaultdict
import pandas as pd

#this function goes through the dataframe and adds the label for the appropriate lowest level account category for each row.


def addLabels(df):
    df['Account Label'] = df.apply(
        lambda x: DentWizard.find_category_by_account(x['ACCOUNT_NUMBER']),
        axis= 1
    )
    return df
"""
testDict = {"Account_Name": ['a', 'b', 'c', 'd', 'e'], "Account_Number":['3080000', '3081000', '3082000', '3310000', '3385000'] }
df = pd.DataFrame(data=testDict)

df['Account Label'] = df.apply(
    lambda x: DentWizard.find_category_by_account(x['Account_Number']),
    axis = 1
)
"""

