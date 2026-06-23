import pandas as pd
import os

from pathlib import Path
DATA_PATH = "D:\\Blue Stock Fintech\\MutualFundAnalytics\\data\\raw"

files = [f for f in os.listdir("D:\\Blue Stock Fintech\\MutualFundAnalytics\\data\\raw") if f.endswith(".csv")]

for file in files:
    print("\n" + "="*60)
    print(f"Dataset: {file}")

    df = pd.read_csv(os.path.join(DATA_PATH, file))

    print("\nShape:")
    print(df.shape)

    print("\nDtypes:")
    print(df.dtypes)

    print("\nHead:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())