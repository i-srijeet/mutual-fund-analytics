import pandas as pd

fund_master = pd.read_csv(
    "../data/raw/01_fund_master.csv"
)

print("\nColumns:")
print(fund_master.columns)

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nRisk Categories:")
print(fund_master["risk_category"].unique())