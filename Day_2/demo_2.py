import pandas as pd
import pandasql as ps

path="emp_hdr.csv"
df=pd.read_csv(path)
print(df)

query="SELECT * from data where sal between 3000 and 5000"
result=ps.sqldf(query,{"data":df})
print("\nResult : \n")
print(result)