import pandas as pd
import pandasql as ps

path="D:\Sunbeam_Internship_GenAI\GIT_Sunbeam\GenAI_94679_11-12-2025\GenAI_94679_11-12-2025\Day_2\emp_hdr.csv"
df=pd.read_csv(path)
print(df)

query="SELECT * from data where sal between 3000 and 5000"
result=ps.sqldf(query,{"data":df})
print("\nResult : \n")
print(result)