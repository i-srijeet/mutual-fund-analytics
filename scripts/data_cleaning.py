import pandas as pd
from pathlib import Path

# =====================================================
# PATHS
# =====================================================

RAW_PATH = Path("D:\\Blue Stock Fintech\\MutualFundAnalytics\\data\\raw")
PROCESSED_PATH = Path("D:\\Blue Stock Fintech\\MutualFundAnalytics\\data\\processed")

PROCESSED_PATH.mkdir(parents=True, exist_ok=True)

# =====================================================
# LOAD DATA
# =====================================================

print("Loading nav_history.csv...")

nav = pd.read_csv(
    RAW_PATH / "02_nav_history.csv"
)

print(f"Original Shape: {nav.shape}")

# =====================================================
# DATA TYPE CONVERSION
# =====================================================

print("\nConverting date column to datetime...")

nav["date"] = pd.to_datetime(
    nav["date"],
    errors="coerce"
)

# Check invalid dates
invalid_dates = nav["date"].isnull().sum()

print(f"Invalid Dates Found: {invalid_dates}")

# =====================================================
# REMOVE INVALID DATE RECORDS
# =====================================================

nav = nav.dropna(subset=["date"])

# =====================================================
# SORT DATA
# =====================================================

print("\nSorting by AMFI code and date...")

nav = nav.sort_values(
    by=["amfi_code", "date"]
)

# =====================================================
# REMOVE DUPLICATES
# =====================================================

duplicates_before = nav.duplicated().sum()

print(f"\nDuplicate Records Found: {duplicates_before}")

nav = nav.drop_duplicates()

duplicates_after = nav.duplicated().sum()

print(f"Duplicate Records After Cleaning: {duplicates_after}")

# =====================================================
# CHECK MISSING NAV VALUES
# =====================================================

missing_nav_before = nav["nav"].isnull().sum()

print(f"\nMissing NAV Before Fill: {missing_nav_before}")

# =====================================================
# FORWARD FILL NAV
# =====================================================

nav["nav"] = nav.groupby(
    "amfi_code"
)["nav"].ffill()

missing_nav_after = nav["nav"].isnull().sum()

print(f"Missing NAV After Fill: {missing_nav_after}")

# =====================================================
# NAV VALIDATION
# =====================================================

invalid_nav = nav[nav["nav"] <= 0]

print(f"\nInvalid NAV Records (<=0): {len(invalid_nav)}")

if len(invalid_nav) > 0:
    print("\nInvalid NAV Sample:")
    print(invalid_nav.head())

# =====================================================
# FINAL DATA QUALITY CHECK
# =====================================================

print("\nFinal Shape:", nav.shape)

print("\nData Types:")
print(nav.dtypes)

# =====================================================
# SAVE CLEANED FILE
# =====================================================

output_file = (
    PROCESSED_PATH /
    "nav_history_clean.csv"
)

nav.to_csv(
    output_file,
    index=False
)

print("\n================================")
print("NAV HISTORY CLEANING COMPLETED")
print("================================")

print(f"Cleaned File Saved At:")
print(output_file)

# =====================================================
# CLEAN INVESTOR_TRANSACTIONS.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING INVESTOR_TRANSACTIONS.CSV")
print("=" * 50)

# Load Dataset
tx = pd.read_csv(
    RAW_PATH / "08_investor_transactions.csv"
)

print(f"\nOriginal Shape: {tx.shape}")

# =====================================================
# STANDARDIZE TRANSACTION TYPES
# =====================================================

tx["transaction_type"] = (
    tx["transaction_type"]
    .astype(str)
    .str.strip()
    .str.upper()
)

# Standardize values
tx["transaction_type"] = tx["transaction_type"].replace({
    "SIP": "SIP",
    "LUMPSUM": "Lumpsum",
    "REDEMPTION": "Redemption"
})

print("\nTransaction Types Found:")
print(tx["transaction_type"].unique())

# =====================================================
# VALIDATE AMOUNT > 0
# =====================================================

invalid_amounts = tx[
    tx["amount_inr"] <= 0
]

print(
    f"\nInvalid Amount Records: {len(invalid_amounts)}"
)

if len(invalid_amounts) > 0:
    print("\nSample Invalid Amounts:")
    print(invalid_amounts.head())

# Remove invalid amounts
tx = tx[
    tx["amount_inr"] > 0
]

# =====================================================
# FIX DATE FORMAT
# =====================================================

tx["transaction_date"] = pd.to_datetime(
    tx["transaction_date"],
    errors="coerce"
)

invalid_dates = (
    tx["transaction_date"]
    .isnull()
    .sum()
)

print(
    f"\nInvalid Transaction Dates: {invalid_dates}"
)

# Remove invalid dates
tx = tx.dropna(
    subset=["transaction_date"]
)

# =====================================================
# VALIDATE KYC STATUS
# =====================================================

print("\nKYC Status Values:")
print(
    tx["kyc_status"]
    .unique()
)

valid_kyc = [
    "Verified",
    "Pending"
]

invalid_kyc = tx[
    ~tx["kyc_status"]
    .isin(valid_kyc)
]

print(
    f"\nInvalid KYC Records: {len(invalid_kyc)}"
)

# =====================================================
# REMOVE DUPLICATES
# =====================================================

duplicates_before = (
    tx.duplicated()
    .sum()
)

print(
    f"\nDuplicate Records Found: {duplicates_before}"
)

tx = tx.drop_duplicates()

duplicates_after = (
    tx.duplicated()
    .sum()
)

print(
    f"Duplicate Records After Cleaning: {duplicates_after}"
)

# =====================================================
# FINAL DATA QUALITY SUMMARY
# =====================================================

print("\nFinal Shape:")
print(tx.shape)

print("\nColumn Data Types:")
print(tx.dtypes)

# =====================================================
# SAVE CLEANED FILE
# =====================================================

output_file = (
    PROCESSED_PATH /
    "investor_transactions_clean.csv"
)

tx.to_csv(
    output_file,
    index=False
)

print("\n================================")
print("INVESTOR TRANSACTIONS CLEANING COMPLETED")
print("================================")

print(
    f"\nCleaned File Saved At:\n{output_file}"
)

# =====================================================
# CLEAN SCHEME_PERFORMANCE.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING SCHEME_PERFORMANCE.CSV")
print("=" * 50)

# Load Dataset
perf = pd.read_csv(
    RAW_PATH / "07_scheme_performance.csv"
)

print(f"\nOriginal Shape: {perf.shape}")

# =====================================================
# VALIDATE RETURN COLUMNS
# =====================================================

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

print("\nConverting return columns to numeric...")

for col in return_cols:
    perf[col] = pd.to_numeric(
        perf[col],
        errors="coerce"
    )

# Check missing values after conversion
print("\nMissing Values in Performance Columns:")

print(
    perf[return_cols]
    .isnull()
    .sum()
)

# =====================================================
# FIND RETURN ANOMALIES
# =====================================================

print("\nChecking Return Anomalies...")

high_return = perf[
    perf["return_1yr_pct"] > 100
]

low_return = perf[
    perf["return_1yr_pct"] < -100
]

print(
    f"Funds with Return > 100% : {len(high_return)}"
)

print(
    f"Funds with Return < -100% : {len(low_return)}"
)

# =====================================================
# EXPENSE RATIO VALIDATION
# =====================================================

print("\nValidating Expense Ratios...")

bad_expense = perf[
    (perf["expense_ratio_pct"] < 0.1)
    |
    (perf["expense_ratio_pct"] > 2.5)
]

print(
    f"Invalid Expense Ratio Records: {len(bad_expense)}"
)

if len(bad_expense) > 0:

    print("\nExpense Ratio Anomalies:")

    print(
        bad_expense[
            [
                "amfi_code",
                "scheme_name",
                "expense_ratio_pct"
            ]
        ]
    )

# =====================================================
# MORNINGSTAR RATING VALIDATION
# =====================================================

print("\nValidating Morningstar Ratings...")

invalid_rating = perf[
    ~perf["morningstar_rating"]
    .between(1, 5)
]

print(
    f"Invalid Ratings Found: {len(invalid_rating)}"
)

# =====================================================
# AUM VALIDATION
# =====================================================

invalid_aum = perf[
    perf["aum_crore"] <= 0
]

print(
    f"\nInvalid AUM Records: {len(invalid_aum)}"
)

# =====================================================
# REMOVE DUPLICATES
# =====================================================

duplicates_before = (
    perf.duplicated()
    .sum()
)

print(
    f"\nDuplicate Records Found: {duplicates_before}"
)

perf = perf.drop_duplicates()

duplicates_after = (
    perf.duplicated()
    .sum()
)

print(
    f"Duplicate Records After Cleaning: {duplicates_after}"
)

# =====================================================
# FINAL DATA QUALITY SUMMARY
# =====================================================

print("\nFinal Shape:")
print(perf.shape)

print("\nColumn Data Types:")
print(perf.dtypes)

# =====================================================
# SAVE CLEANED DATA
# =====================================================

output_file = (
    PROCESSED_PATH /
    "scheme_performance_clean.csv"
)

perf.to_csv(
    output_file,
    index=False
)

print("\n================================")
print("SCHEME PERFORMANCE CLEANING COMPLETED")
print("================================")

print(
    f"\nCleaned File Saved At:\n{output_file}"
)

# =====================================================
# CLEAN FUND_MASTER.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING FUND_MASTER.CSV")
print("=" * 50)

fund = pd.read_csv(
    RAW_PATH / "01_fund_master.csv"
)

print(f"\nOriginal Shape: {fund.shape}")

# Remove duplicates

duplicates = fund.duplicated().sum()

print(
    f"\nDuplicate Records: {duplicates}"
)

fund = fund.drop_duplicates()

# Validate AMFI Code

invalid_amfi = fund[
    fund["amfi_code"] <= 0
]

print(
    f"\nInvalid AMFI Codes: {len(invalid_amfi)}"
)

# Validate Expense Ratio

bad_expense = fund[
    (fund["expense_ratio_pct"] < 0)
]

print(
    f"\nInvalid Expense Ratios: {len(bad_expense)}"
)

# Convert Launch Date

fund["launch_date"] = pd.to_datetime(
    fund["launch_date"],
    errors="coerce"
)

invalid_dates = (
    fund["launch_date"]
    .isnull()
    .sum()
)

print(
    f"\nInvalid Launch Dates: {invalid_dates}"
)

# Save

fund.to_csv(
    PROCESSED_PATH /
    "fund_master_clean.csv",
    index=False
)

print(
    "\nFund Master Cleaning Completed"
)

# =====================================================
# CLEAN AUM_BY_FUND_HOUSE.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING AUM_BY_FUND_HOUSE.CSV")
print("=" * 50)

aum = pd.read_csv(
    RAW_PATH / "03_aum_by_fund_house.csv"
)

print(f"\nOriginal Shape: {aum.shape}")

# Convert Date

aum["date"] = pd.to_datetime(
    aum["date"],
    errors="coerce"
)

invalid_dates = (
    aum["date"]
    .isnull()
    .sum()
)

print(
    f"\nInvalid Dates: {invalid_dates}"
)

# Remove Duplicates

duplicates = (
    aum.duplicated()
    .sum()
)

print(
    f"\nDuplicate Records: {duplicates}"
)

aum = aum.drop_duplicates()

# Validate AUM

invalid_aum = aum[
    aum["aum_crore"] <= 0
]

print(
    f"\nInvalid AUM Records: {len(invalid_aum)}"
)

# Validate Scheme Count

invalid_schemes = aum[
    aum["num_schemes"] <= 0
]

print(
    f"\nInvalid Scheme Count Records: {len(invalid_schemes)}"
)

# Save

aum.to_csv(
    PROCESSED_PATH /
    "aum_by_fund_house_clean.csv",
    index=False
)

print(
    "\nAUM BY FUND HOUSE CLEANING COMPLETED"
)

# =====================================================
# CLEAN MONTHLY_SIP_INFLOWS.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING MONTHLY_SIP_INFLOWS.CSV")
print("=" * 50)

sip = pd.read_csv(
    RAW_PATH / "04_monthly_sip_inflows.csv"
)

print(f"\nOriginal Shape: {sip.shape}")

# Convert Month

sip["month"] = pd.to_datetime(
    sip["month"],
    format="%Y-%m",
    errors="coerce"
)

invalid_months = (
    sip["month"]
    .isnull()
    .sum()
)

print(
    f"\nInvalid Month Values: {invalid_months}"
)

# Remove Duplicates

duplicates = (
    sip.duplicated()
    .sum()
)

print(
    f"\nDuplicate Records: {duplicates}"
)

sip = sip.drop_duplicates()

# Validate Numeric Fields

numeric_cols = [
    "sip_inflow_crore",
    "active_sip_accounts_crore",
    "new_sip_accounts_lakh",
    "sip_aum_lakh_crore"
]

for col in numeric_cols:

    invalid = sip[
        sip[col] < 0
    ]

    print(
        f"Invalid {col}: {len(invalid)}"
    )

# Keep YoY NULL values
# They are expected for first year

print(
    f"\nMissing YoY Values: "
    f"{sip['yoy_growth_pct'].isnull().sum()}"
)

# Save

sip.to_csv(
    PROCESSED_PATH /
    "monthly_sip_inflows_clean.csv",
    index=False
)

print(
    "\nMONTHLY SIP INFLOWS CLEANING COMPLETED"
)

# =====================================================
# CLEAN CATEGORY_INFLOWS.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING CATEGORY_INFLOWS.CSV")
print("=" * 50)

cat = pd.read_csv(
    RAW_PATH / "05_category_inflows.csv"
)

print(f"\nOriginal Shape: {cat.shape}")

cat["month"] = pd.to_datetime(
    cat["month"],
    format="%Y-%m",
    errors="coerce"
)

print(
    f"\nInvalid Months: "
    f"{cat['month'].isnull().sum()}"
)

duplicates = cat.duplicated().sum()

print(
    f"\nDuplicate Records: {duplicates}"
)

cat = cat.drop_duplicates()

print(
    f"\nMissing Categories: "
    f"{cat['category'].isnull().sum()}"
)

cat.to_csv(
    PROCESSED_PATH /
    "category_inflows_clean.csv",
    index=False
)

print(
    "\nCATEGORY INFLOWS CLEANING COMPLETED"
)

# =====================================================
# CLEAN INDUSTRY_FOLIO_COUNT.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING INDUSTRY_FOLIO_COUNT.CSV")
print("=" * 50)

folio = pd.read_csv(
    RAW_PATH / "06_industry_folio_count.csv"
)

print(f"\nOriginal Shape: {folio.shape}")

folio["month"] = pd.to_datetime(
    folio["month"],
    format="%Y-%m",
    errors="coerce"
)

print(
    f"\nInvalid Months: "
    f"{folio['month'].isnull().sum()}"
)

duplicates = folio.duplicated().sum()

print(
    f"\nDuplicate Records: {duplicates}"
)

folio = folio.drop_duplicates()

numeric_cols = [
    "total_folios_crore",
    "equity_folios_crore",
    "debt_folios_crore",
    "hybrid_folios_crore",
    "others_folios_crore"
]

for col in numeric_cols:

    invalid = folio[
        folio[col] < 0
    ]

    print(
        f"Invalid {col}: {len(invalid)}"
    )

folio.to_csv(
    PROCESSED_PATH /
    "industry_folio_count_clean.csv",
    index=False
)

print(
    "\nINDUSTRY FOLIO COUNT CLEANING COMPLETED"
)

# =====================================================
# CLEAN PORTFOLIO_HOLDINGS.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING PORTFOLIO_HOLDINGS.CSV")
print("=" * 50)

holdings = pd.read_csv(
    RAW_PATH / "09_portfolio_holdings.csv"
)

print(f"\nOriginal Shape: {holdings.shape}")

holdings["portfolio_date"] = pd.to_datetime(
    holdings["portfolio_date"],
    errors="coerce"
)

print(
    f"\nInvalid Portfolio Dates: "
    f"{holdings['portfolio_date'].isnull().sum()}"
)

duplicates = holdings.duplicated().sum()

print(
    f"\nDuplicate Records: {duplicates}"
)

holdings = holdings.drop_duplicates()

invalid_weight = holdings[
    (holdings["weight_pct"] < 0)
    |
    (holdings["weight_pct"] > 100)
]

print(
    f"\nInvalid Weight Records: "
    f"{len(invalid_weight)}"
)

invalid_price = holdings[
    holdings["current_price_inr"] <= 0
]

print(
    f"Invalid Price Records: "
    f"{len(invalid_price)}"
)

holdings.to_csv(
    PROCESSED_PATH /
    "portfolio_holdings_clean.csv",
    index=False
)

print(
    "\nPORTFOLIO HOLDINGS CLEANING COMPLETED"
)

# =====================================================
# CLEAN BENCHMARK_INDICES.CSV
# =====================================================

print("\n" + "=" * 50)
print("CLEANING BENCHMARK_INDICES.CSV")
print("=" * 50)

bench = pd.read_csv(
    RAW_PATH / "10_benchmark_indices.csv"
)

print(f"\nOriginal Shape: {bench.shape}")

bench["date"] = pd.to_datetime(
    bench["date"],
    errors="coerce"
)

print(
    f"\nInvalid Dates: "
    f"{bench['date'].isnull().sum()}"
)

duplicates = bench.duplicated().sum()

print(
    f"\nDuplicate Records: {duplicates}"
)

bench = bench.drop_duplicates()

invalid_close = bench[
    bench["close_value"] <= 0
]

print(
    f"\nInvalid Close Values: "
    f"{len(invalid_close)}"
)

print(
    "\nUnique Benchmarks:"
)

print(
    bench["index_name"]
    .unique()
)

bench.to_csv(
    PROCESSED_PATH /
    "benchmark_indices_clean.csv",
    index=False
)

print(
    "\nBENCHMARK INDICES CLEANING COMPLETED"
)