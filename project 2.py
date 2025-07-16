#%%
import numpy as np
import pandas as pd
np.random.seed(42)
employee_ids=[f"EMP_{i:03d}" for i in range (1,31)]
dates=pd.date_range(start="2025-07-01",periods=30,freq="D")
employee_ids
data={
    "Date":np.tile(dates,len(employee_ids)),
    "Employee_ID":np.repeat(employee_ids,len(dates)),
    "Working_Hours":np.random.uniform(4,10,size=len(dates)*len(employee_ids)).round(2)}
df=pd.DataFrame(data)
df.to_csv("employee_working_hours.csv", index=False)
df_csv=pd.read_csv("employee_working_hours.csv")
print(df_csv.head())
print(df_csv.describe())
print(df_csv["Employee_ID"].nunique())
total_hours=df_csv.groupby("Employee_ID")["Working_Hours"].sum().sort_values(ascending=False)
avg_daily= df_csv.groupby("Employee_ID")["Working_Hours"].mean()
threshold_low=5
threshold_high=9
df_csv["Low_Hour_Flag"]=df_csv["Working_Hours"]<threshold_low
df_csv["High_Hour_Flag"]=df_csv["Working_Hours"]>threshold_high
print(df_csv[df_csv["Low_Hour_Flag"]|df_csv["High_Hour_Flag"]].head())

#%%

import matplotlib.pyplot as plt
import seaborn as sns
top10=total_hours.head(10)
plt.figure(figsize=(10, 5))
sns.barplot(x=top10.index, y=top10.values)
plt.xticks(rotation=45)
plt.title("Top 10 Employees by Total working hours")
plt.ylabel("Hours")
plt.tight_layout()
plt.show()
