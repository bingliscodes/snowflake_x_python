from connection_test import *
import matplotlib.pyplot as plt
"""
Cost is 
1. Get all cost and product data by district from April 23, 2023 to Feb 29, 2024

Cost is Parts (4015000) and OEM Parts (4015500) lines from P&L 
Revenue is comprised of:
a) sublet parts revenue (3080000)
b) mechanical parts revenue (product_rev test with appropriate filters in Snowflake)
c) paint parts revenue (product_rev test with appropriate filters in Snowflake)

2. Load into 2 data frames (one for cost, one for rev)
3. Graph time series by district
"""

#Connect
dataframe = None
connection_params = {
    'user': os.getenv('SNOWFLAKE_USER'),
    'password': os.getenv('DW_PASSWORD'),
    'account': os.getenv('DW_ACCOUNT'),
    'warehouse': os.getenv('SNOWFLAKE_WAREHOUSE'),
    'database': os.getenv('SNOWFLAKE_DATABASE'),
    #'schema': os.getenv('SNOWFLAKE_SCHEMA'),
    }
    # Establishing connection
connection = snowflake.connector.connect(
    user=connection_params['user'],
    password=connection_params['password'],
    account=connection_params['account'],
    warehouse=connection_params['warehouse'],
    database=connection_params['database'],
    #schema=connection_params['schema'],
    authenticator='snowflake',
)


    # Creating a cursor object
cur = connection.cursor()

cost_query = """
SELECT * FROM DEPT_FINANCE.PUBLIC.PARTS_COST
"""
revenue_query = """
SELECT * FROM DEPT_FINANCE.PUBLIC.PRODUCT_REV_TEST
"""
sublet_query = """
SELECT * FROM DEPT_FINANCE.PUBLIC.SUBLET_REV_LOOKUP
"""
def execute_query_and_fetch_df(query):
    try:
        cur.execute(query)
        data = cur.fetch_pandas_all()
        return data
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

df_cost = execute_query_and_fetch_df(cost_query)
df_revenue = execute_query_and_fetch_df(revenue_query)
df_sublet_rev = execute_query_and_fetch_df(sublet_query)    

#Clean the data

columns_needed = ['Division', 'District', 'Revenue', 'Account Period']
divisions_to_exclude = ['Unknown', 'Key Operations']
df_revenue_filtered = df_revenue[columns_needed]
df_revenue_filtered = df_revenue_filtered[~df_revenue_filtered['Division'].isin(divisions_to_exclude)]
df_sublet_rev_filtered = df_sublet_rev[columns_needed]


df_rev = pd.concat([df_revenue_filtered, df_sublet_rev_filtered], ignore_index = True)
df_rev = df_rev[~df_rev['Division'].isin(divisions_to_exclude)]
df_cost = df_cost[~df_cost['Division'].isin(divisions_to_exclude)]
# Check for NaN values
#print(df_rev.isnull().sum())

#fill NaN values with a default value or drop them
#df_rev.fillna(0, inplace=True)  # This fills NaN values with 0 #or
# This removes rows with NaN values
df_rev.dropna(inplace=True)
df_cost.dropna(inplace=True)

df_rev['Revenue'] = pd.to_numeric(df_rev['Revenue'], errors='coerce')
df_rev['Account Period'] = pd.to_datetime(df_rev['Account Period'])
df_rev['YearMonth'] = df_rev['Account Period'].dt.to_period('M')
monthly_rev_data_district = df_rev.groupby(['YearMonth', 'District'])['Revenue'].sum().reset_index()
monthly_rev_data_division = df_rev.groupby(['YearMonth', 'Division'])['Revenue'].sum().reset_index()


df_cost['Cost'] = pd.to_numeric(df_cost['Cost'], errors='coerce')
df_cost['Account Period'] = pd.to_datetime(df_cost['Account Period'])
df_cost['YearMonth'] = df_cost['Account Period'].dt.to_period('M')
monthly_cost_data_district = df_cost.groupby(['YearMonth', 'District'])['Cost'].sum().reset_index()
monthly_cost_data_division = df_cost.groupby(['YearMonth', 'Division'])['Cost'].sum().reset_index()

# Merging the data on 'YearMonth' and 'Division'
merged_data = pd.merge(monthly_cost_data_division, monthly_rev_data_division, on=['YearMonth', 'Division'], how='outer')
# Calculate the cost to revenue ratio with safety for division by zero
merged_data['Cost_to_Revenue_Ratio'] = merged_data.apply(
    lambda row: row['Cost'] / row['Revenue'] if row['Revenue'] != 0 else None, axis=1)


####Division Plot - Just ratio#####
merged_data['YearMonth_str'] = merged_data['YearMonth'].astype(str)

plt.figure(figsize=(14,8))

for division in merged_data['Division'].unique():
    division_data = merged_data[merged_data['Division'] == division]
    plt.plot(division_data['YearMonth_str'], division_data['Cost_to_Revenue_Ratio'], label=division, marker='o', linestyle='--')

plt.title('Cost-to-Revenue Ratio by Division Over Time')
plt.xlabel('Year-Month')
plt.ylabel('Cost-to-Revenue Ratio')
plt.xticks(rotation=45)
plt.legend(title='Division', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)  # Optional: Adds a grid for better readability
plt.tight_layout()
plt.show()

exit()
###DIVISION PLOTS -- COMBINED######

# fig, ax1 = plt.subplots(figsize=(14, 8))

# # Ensure 'YearMonth' is converted to string for plotting purposes
# merged_data['YearMonth_str'] = merged_data['YearMonth'].astype(str)

# # Loop through each division and plot cost and revenue on ax1
# for division in merged_data['Division'].unique():
#     division_data = merged_data[merged_data['Division'] == division]
#     ax1.plot(division_data['YearMonth_str'], division_data['Cost'], label=f'Cost - {division}', marker='o')
#     ax1.plot(division_data['YearMonth_str'], division_data['Revenue'], label=f'Revenue - {division}', linestyle='--', marker='x')

# # Set labels and title for ax1
# ax1.set_xlabel('Year-Month')
# ax1.set_ylabel('Amount (USD)')
# ax1.tick_params(axis='x', rotation=45)
# ax1.set_title('Monthly Cost, Revenue, and Cost-to-Revenue Ratio by Division')

# # Create ax2 for the cost-to-revenue ratio with a shared x-axis
# ax2 = ax1.twinx()  
# ax2.set_ylabel('Cost-to-Revenue Ratio')

# # Plot cost-to-revenue ratio on ax2, also using 'YearMonth_str'
# for division in merged_data['Division'].unique():
#     division_data = merged_data[merged_data['Division'] == division]
#     ax2.plot(division_data['YearMonth_str'], division_data['Cost_to_Revenue_Ratio'], label=f'Ratio - {division}', linestyle=':', marker='s', linewidth=2)

# # Combine legends from both y-axes for clarity
# lines, labels = ax1.get_legend_handles_labels()
# lines2, labels2 = ax2.get_legend_handles_labels()
# ax2.legend(lines + lines2, labels + labels2, loc='upper left', bbox_to_anchor=(1.1, 1))

# plt.tight_layout()
# plt.show()

exit()
###### DISTRICT PLOTS ######
plt.figure(figsize=(12,8))

if monthly_cost_data_district is not None and not monthly_cost_data_district.empty:
    for district, group in monthly_cost_data_district.groupby('District'):
        group['YearMonth'] = group['YearMonth'].astype(str)
        plt.plot(group['YearMonth'], group['Cost'], label=district)

    plt.title('Cost by District Over Time')
    plt.xlabel('Year-Month')
    plt.ylabel('Cost')
    plt.xticks(rotation=45)
    plt.legend(title='District', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend placement to avoid overlap
    plt.tight_layout()  # Adjust layout to make room for the legend
    plt.show()

if monthly_rev_data_district is not None and not monthly_rev_data_district.empty:
    for district, group in monthly_rev_data_district.groupby('District'):
        group['YearMonth'] = group['YearMonth'].astype(str)
        plt.plot(group['YearMonth'], group['Revenue'], label=district)

    plt.title('Revenue by District Over Time')
    plt.xlabel('Year-Month')
    plt.ylabel('Revenue')
    plt.xticks(rotation=45)
    plt.legend(title='District', bbox_to_anchor=(1.05, 1), loc='upper left')  # Adjust legend placement to avoid overlap
    plt.tight_layout()  # Adjust layout to make room for the legend
    plt.show()



cur.close()
connection.close()

