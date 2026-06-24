-- =====================================================
-- DIMENSION TABLES
-- =====================================================

CREATE TABLE dim_fund (
amfi_code INTEGER PRIMARY KEY,
scheme_name TEXT NOT NULL,
fund_house TEXT,
category TEXT,
sub_category TEXT,
plan TEXT,
risk_category TEXT
);

CREATE TABLE dim_date (
date_key INTEGER PRIMARY KEY,
full_date DATE NOT NULL,
year INTEGER,
quarter INTEGER,
month INTEGER,
month_name TEXT
);

-- =====================================================
-- FACT TABLES
-- =====================================================

CREATE TABLE fact_nav (
nav_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER NOT NULL,
nav_date DATE NOT NULL,
nav REAL NOT NULL,

```
FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
```

);

CREATE TABLE fact_transactions (
transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
investor_id TEXT,
amfi_code INTEGER,
transaction_date DATE,
transaction_type TEXT,
amount_inr REAL,
state TEXT,
city TEXT,
kyc_status TEXT,

```
FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
```

);

CREATE TABLE fact_performance (
performance_id INTEGER PRIMARY KEY AUTOINCREMENT,
amfi_code INTEGER,
return_1yr_pct REAL,
return_3yr_pct REAL,
return_5yr_pct REAL,
benchmark_3yr_pct REAL,
alpha REAL,
beta REAL,
sharpe_ratio REAL,
expense_ratio_pct REAL,
aum_crore REAL,

```
FOREIGN KEY (amfi_code)
    REFERENCES dim_fund(amfi_code)
```

);

CREATE TABLE fact_aum (
aum_id INTEGER PRIMARY KEY AUTOINCREMENT,
fund_house TEXT,
aum_date DATE,
aum_crore REAL,
num_schemes INTEGER
);
