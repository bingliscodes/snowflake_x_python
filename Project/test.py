import pandas as pd
from datetime import date
data_frame1 = pd.DataFrame({'Fruits': ['Appple', 'Banana', 'Mango',
                                       'Dragon Fruit', 'Musk melon', 'grapes'],
                            'Sales in kg': [20, 30, 15, 10, 50, 40]})
 
# create  data_frame2 by creating a dictionary 
# in which values are stored as list
data_frame2 = pd.DataFrame({'Vegetables': ['tomato', 'Onion', 'ladies finger',
                                           'beans', 'bedroot', 'carrot'],
                            'Sales in kg': [200, 310, 115, 110, 55, 45]})
 
# create  data_frame3 by creating a dictionary 
# in which values are stored as list
data_frame3 = pd.DataFrame({'Baked Items': ['Cakes', 'biscuits', 'muffins',
                                            'Rusk', 'puffs', 'cupcakes'],
                            'Sales in kg': [120, 130, 159, 310, 150, 140]})
#Step 3: save as csv and email
file_name = "Carmax Product Summary Report - " + date.today().strftime("%m%y") + "xlsx"

with pd.ExcelWriter(file_name) as writer:
    data_frame1.to_excel(writer, sheet_name="1", index=False)
    data_frame2.to_excel(writer, sheet_name="2", index=False)