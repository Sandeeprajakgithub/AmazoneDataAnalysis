import pandas as pd

t1_df = pd.read_excel("Amzaone Sale file 1.xlsx")
t2_df = pd.read_excel("Amzaone Sale file 2.xlsx")

#merging data here
merge_df =  pd.merge(t1_df,t2_df,on='Order ID',how='outer')


#finding columns
t1_columns = t1_df.columns
t2_columns = t2_df.columns

#iteration over columns
for column in t2_columns:
    if column not in  t1_columns:
        #please mension your conditions here of data joinning 
        
t1_df.to_excel("merged_Result.xlsx",index=False)





