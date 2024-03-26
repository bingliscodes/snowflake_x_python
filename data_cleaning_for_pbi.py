#data_cleaning_for_pbi.py
from metrics_test import *
from account_organization import *

#THIS WORKS FOR DIVISION LEVEL
def aggregate_metrics(df, account_dict, amount_column, levels=None):
    aggregated_data = []
    for metric, account_numbers in account_dict.items():
        # Filter by account numbers
        filtered_df = df[df['Account Number'].isin(account_numbers)]
        
        # Determine the grouping columns based on provided levels
        grouping_columns = ['Account Period']
        if levels is not None and isinstance(levels, list):
            grouping_columns.extend(levels)

        # Group by the specified levels along with 'Account Period', sum the amounts
        grouped = filtered_df.groupby(grouping_columns)[amount_column].sum().reset_index()

        # Add the metric name to each row in the grouped DataFrame
        grouped['Metric'] = metric

        # Append the grouped data to the aggregated data list
        aggregated_data.append(grouped)

    # Concatenate all the aggregated dataframes into one
    return pd.concat(aggregated_data, ignore_index=True)

#Prepare the Actuals and Budgets DataFrames
actuals_df = execute_query_and_load_data(actuals_query)

aggregated_actuals = aggregate_metrics(
    actuals_df,
    account_dict,
    'Net Sign Rev',
    levels=['Division', 'District', 'Department']
)


budget_df = execute_query_and_load_data(budget_query)
budget_df.loc[budget_df['Account Type'].isin(expense_accounts), 'Budget Amount USD'] *= -1
aggregated_budgets = aggregate_metrics(
    budget_df,
    account_dict,
    'Budget Amount USD',
    levels=['Division', 'District', 'Department']
)

aggregated_actuals.to_csv('actuals_v2.csv')
aggregated_budgets.to_csv('budget_v2.csv')

