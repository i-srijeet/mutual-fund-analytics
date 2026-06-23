import pandas as pd

fund_master = pd.read_csv("../data/raw/01_fund_master.csv")
nav_history = pd.read_csv("../data/raw/02_nav_history.csv")
scheme_perf = pd.read_csv("../data/raw/07_scheme_performance.csv")
portfolio = pd.read_csv("../data/raw/09_portfolio_holdings.csv")

master_codes = set(fund_master["amfi_code"])

print("\nNAV Validation")
print(master_codes - set(nav_history["amfi_code"]))

print("\nPerformance Validation")
print(master_codes - set(scheme_perf["amfi_code"]))

print("\nPortfolio Validation")
print(master_codes - set(portfolio["amfi_code"]))

missing_codes = master_codes - set(portfolio["amfi_code"])

print("\nMissing Portfolio Schemes:\n")

for code in missing_codes:
    row = fund_master[
        fund_master["amfi_code"] == code
    ]

    print(
        code,
        "-",
        row["scheme_name"].values[0]
    )