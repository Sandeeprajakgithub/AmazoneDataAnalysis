#now here we will push our data into my mysql server using python script and then we will import that so our 
# dashboard will be more dynamic

import pandas as pd
from sqlalchemy import create_engine
import mysql.connector

host = 'localhost'  
# Please enter you host name of your Virtual Machine if your want to send data in virtual Database 
# like - 40.30.150.11

port = 3306
database = 'mydb'
username = 'root'
password = '1234'
excel_file_name = 'Merged_Result.xlsx'
mysql_table_name = 'datatableforsalesamazone'

#we need to create our connections string first here
connection_str =  f'mysql+mysqlconnector://{username}:{password}@{host}:{port}/{database}'
# now add one connector of sql
df = pd.read_excel(excel_file_name)


engine = create_engine(connection_str)
df.to_sql("datatable",con=engine,if_exists='replace',index=False)

print("data inserted successfully")


# since we are facing no module issue that why we will install a new libera...
# pip install mysql-connector-python

