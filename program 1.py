#%%
import numpy as np
import pandas as pd
from packaging.tags import platform_tags

np.random.seed(42)
apartments=[f"apy_{i}" for i in range (1,21)]
dates=pd.date_range(start="2025-07-01",periods=30,freq="D")
data={
    "Date":np.tile(dates,len(apartments)),
    "Apartment":np.repeat(apartments,len(dates)),
    "Electricity_usage":np.random.normal(loc=20,scale=5,size=len(dates)*len(apartments))}
df=pd.DataFrame(data)
df
df["Electricity_usage"]=df["Electricity_usage"].round(2)
df
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
usage_per_apartment=df.groupby("Apartment")["Electricity_usage"].sum().sort_values(ascending=False)
print(usage_per_apartment)
daily_avg=df.groupby("Date")["Electricity_usage"].mean()
print(daily_avg.head())

#%%
pip install matplotlib
#%%
pip install seaborn
#%%
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(10,6))
sns.barplot(x=usage_per_apartment.index, y=usage_per_apartment.values)
plt.xticks(rotation=90)
plt.title("Total usage per Apartments")
plt.xlabel("Apartment")
plt.ylabel("Total KWH")
plt.tight_layout()
plt.show()

#%%
plt.figure(figsize=(10,6))
sns.lineplot(x=daily_avg.index,y=daily_avg.values)
plt.title("Daily average electicity usage")
plt.xlabel("Date")
plt.ylabel("Total Kwh")
plt.tight_layout()
plt.show()
#%%
threshold=df["Electricity_usage"].mean()+2 *df["Electricity_usage"].std()
df["High_usage_flag"]=df["Electricity_usage"]>threshold
print(df[df["High_usage_flag"]== True].head())