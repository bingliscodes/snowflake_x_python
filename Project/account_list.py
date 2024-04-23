
def generate_sql_inserts(file_path):
    metric_name = ''
    values_list = []

    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            if line.endswith('{'):
                metric_name = line[:-1].strip()
            elif line.startswith("'") and metric_name:
                account_numbers = line.rstrip(",}").strip("'").split("', '")
                for account_number in account_numbers:
                    values_entry = f"('{metric_name}', '{account_number}')"
                    values_list.append(values_entry)
            elif line == '}':
                metric_name = ''

    # Build the SQL insert statement separately to avoid the syntax error
    values_str = ",\n".join(values_list)
    sql_insert = "INSERT INTO MeasureMapping (MeasureName, AccountNumber) VALUES\n" + values_str + ";"
    return sql_insert

# Assuming the file is named 'account_list.txt' and located in the same directory as this script
file_path = 'account_list.txt'
sql_inserts = generate_sql_inserts(file_path)

print(sql_inserts)
