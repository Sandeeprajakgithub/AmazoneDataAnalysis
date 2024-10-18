import pandas as pd

table1_df = pd.read_excel("Amzaone Sale file 1.xlsx")
table2_df = pd.read_excel("Amzaone Sale file 2.xlsx")

merged_df = pd.merge(table1_df, table2_df, on='Order ID', how='left')

# table1_columns = table1_df.columns
# table2_columns = table2_df.columns

# for column in table2_df.columns:
#     if column not in table1_df.columns:
#         table1_df[column] = table2_df[column]
merged_df.to_excel("merged_table.xlsx", index=False)
