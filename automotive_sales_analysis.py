import pandas as pd

# Load dataset
df = pd.read_csv("automotive_sales.csv")

# Basic cleaning
df.drop_duplicates(inplace=True)
df.fillna(0, inplace=True)

# Revenue by region
region_sales = df.groupby("Region")["Revenue"].sum().reset_index()

# Top selling models
top_models = df.groupby("Model")["Revenue"].sum().sort_values(ascending=False).head(10)

print(region_sales)
print(top_models)
