from metrics_test import *

def aggregate_metrics(data, account_dict, amount_column):
    aggregated_data = []

    for metric, account_numbers in account_dict.items():
        filtered_df = data[data['Account Number'].isin(account_numbers)]

        grouped = filtered_df.groupby('Account Period')[amount_column].sum().reset_index()

        grouped['Metric'] = metric
        
        aggregated_data.append(grouped)

    return pd.concat(aggregated_data, ignore_index=True)

actuals_df = execute_query_and_load_data(actuals_query)
# Assume 'Net Sign Rev' is the amount column for actuals
aggregated_actuals = aggregate_metrics(actuals_df, account_dict, 'Net Sign Rev')

#Prepare the Actuals and Budgets DataFrames
budget_df = execute_query_and_load_data(budget_query)
# Adjust budget amounts as you've already done
budget_df.loc[budget_df['Account Type'].isin(expense_accounts), 'Budget Amount USD'] *= -1
# Assume the budget amount column is 'Budget Amount USD'
aggregated_budgets = aggregate_metrics(budget_df, account_dict, 'Budget Amount USD')

#Combine the Actuals and Budgets
aggregated_actuals['Type'] = 'Actual'
aggregated_budgets['Type'] = 'Budget'

combined_df = pd.concat([aggregated_actuals, aggregated_budgets], ignore_index=True)
combined_df.to_csv('results.csv')

