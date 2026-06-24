# Mutual Fund Analytics Platform - Data Dictionary

## Overview

This document describes all datasets used in the Mutual Fund Analytics Platform project, including column definitions, data types, business meaning, and source references.

---

# 1. fund_master.csv

**Source:** AMFI Scheme Master Dataset

| Column             | Data Type | Business Definition                        |
| ------------------ | --------- | ------------------------------------------ |
| amfi_code          | INTEGER   | Unique AMFI scheme identifier              |
| fund_house         | TEXT      | Asset Management Company (AMC)             |
| scheme_name        | TEXT      | Mutual fund scheme name                    |
| category           | TEXT      | Broad scheme category (Equity, Debt, etc.) |
| sub_category       | TEXT      | Detailed fund classification               |
| plan               | TEXT      | Direct or Regular Plan                     |
| launch_date        | DATE      | Scheme launch date                         |
| benchmark          | TEXT      | Benchmark index used for comparison        |
| expense_ratio_pct  | REAL      | Annual expense ratio (%)                   |
| exit_load_pct      | REAL      | Exit load charged on redemption            |
| min_sip_amount     | INTEGER   | Minimum SIP investment amount              |
| min_lumpsum_amount | INTEGER   | Minimum lump-sum investment                |
| fund_manager       | TEXT      | Scheme fund manager                        |
| risk_category      | TEXT      | Risk classification                        |
| sebi_category_code | TEXT      | SEBI category identifier                   |

---

# 2. nav_history.csv

**Source:** Historical NAV Dataset

| Column    | Data Type | Business Definition           |
| --------- | --------- | ----------------------------- |
| amfi_code | INTEGER   | Scheme identifier             |
| date      | DATE      | NAV date                      |
| nav       | REAL      | Net Asset Value of the scheme |

---

# 3. aum_by_fund_house.csv

**Source:** Industry AUM Statistics

| Column           | Data Type | Business Definition                 |
| ---------------- | --------- | ----------------------------------- |
| date             | DATE      | Reporting date                      |
| fund_house       | TEXT      | Asset management company            |
| aum_crore        | REAL      | Assets Under Management (Crore INR) |
| market_share_pct | REAL      | Industry market share percentage    |
| num_schemes      | INTEGER   | Number of active schemes            |

---

# 4. monthly_sip_inflows.csv

**Source:** SIP Industry Statistics

| Column                    | Data Type | Business Definition                  |
| ------------------------- | --------- | ------------------------------------ |
| month                     | DATE      | Reporting month                      |
| sip_inflow_crore          | REAL      | Monthly SIP inflow amount            |
| active_sip_accounts_crore | REAL      | Active SIP accounts                  |
| new_sip_accounts_lakh     | REAL      | Newly registered SIP accounts        |
| sip_aum_lakh_crore        | REAL      | SIP assets under management          |
| yoy_growth_pct            | REAL      | Year-over-year SIP growth percentage |

---

# 5. category_inflows.csv

**Source:** Mutual Fund Category Statistics

| Column           | Data Type | Business Definition       |
| ---------------- | --------- | ------------------------- |
| month            | DATE      | Reporting month           |
| category         | TEXT      | Fund category             |
| net_inflow_crore | REAL      | Net inflow/outflow amount |

---

# 6. industry_folio_count.csv

**Source:** Industry Folio Statistics

| Column              | Data Type | Business Definition    |
| ------------------- | --------- | ---------------------- |
| month               | DATE      | Reporting month        |
| total_folios_crore  | REAL      | Total industry folios  |
| equity_folios_crore | REAL      | Equity category folios |
| debt_folios_crore   | REAL      | Debt category folios   |
| hybrid_folios_crore | REAL      | Hybrid category folios |
| others_folios_crore | REAL      | Other category folios  |

---

# 7. scheme_performance.csv

**Source:** Scheme Performance Dataset

| Column             | Data Type | Business Definition                |
| ------------------ | --------- | ---------------------------------- |
| amfi_code          | INTEGER   | Scheme identifier                  |
| scheme_name        | TEXT      | Mutual fund scheme name            |
| fund_house         | TEXT      | Asset management company           |
| category           | TEXT      | Fund category                      |
| plan               | TEXT      | Direct or Regular                  |
| return_1yr_pct     | REAL      | One-year return (%)                |
| return_3yr_pct     | REAL      | Three-year return (%)              |
| return_5yr_pct     | REAL      | Five-year return (%)               |
| benchmark_3yr_pct  | REAL      | Benchmark 3-year return            |
| alpha              | REAL      | Risk-adjusted excess return        |
| beta               | REAL      | Volatility relative to benchmark   |
| sharpe_ratio       | REAL      | Risk-adjusted performance measure  |
| sortino_ratio      | REAL      | Downside-risk-adjusted performance |
| std_dev_ann_pct    | REAL      | Annualized standard deviation      |
| max_drawdown_pct   | REAL      | Maximum observed decline           |
| aum_crore          | REAL      | Assets Under Management            |
| expense_ratio_pct  | REAL      | Expense ratio percentage           |
| morningstar_rating | INTEGER   | Morningstar rating (1–5)           |
| risk_grade         | TEXT      | Risk classification                |

---

# 8. investor_transactions.csv

**Source:** Investor Activity Dataset

| Column             | Data Type | Business Definition        |
| ------------------ | --------- | -------------------------- |
| investor_id        | TEXT      | Unique investor identifier |
| transaction_date   | DATE      | Transaction date           |
| amfi_code          | INTEGER   | Scheme identifier          |
| transaction_type   | TEXT      | SIP, Lumpsum, Redemption   |
| amount_inr         | REAL      | Transaction amount         |
| state              | TEXT      | Investor state             |
| city               | TEXT      | Investor city              |
| city_tier          | TEXT      | Tier classification        |
| age_group          | TEXT      | Investor age bracket       |
| gender             | TEXT      | Investor gender            |
| annual_income_lakh | REAL      | Annual income in lakhs     |
| payment_mode       | TEXT      | Payment channel            |
| kyc_status         | TEXT      | KYC verification status    |

---

# 9. portfolio_holdings.csv

**Source:** Portfolio Holdings Dataset

| Column            | Data Type | Business Definition      |
| ----------------- | --------- | ------------------------ |
| amfi_code         | INTEGER   | Scheme identifier        |
| portfolio_date    | DATE      | Portfolio reporting date |
| stock_symbol      | TEXT      | Equity ticker symbol     |
| company_name      | TEXT      | Invested company name    |
| sector            | TEXT      | Industry sector          |
| weight_pct        | REAL      | Portfolio weight (%)     |
| shares_held       | REAL      | Shares held              |
| current_price_inr | REAL      | Market price per share   |

---

# 10. benchmark_indices.csv

**Source:** Market Benchmark Dataset

| Column      | Data Type | Business Definition  |
| ----------- | --------- | -------------------- |
| date        | DATE      | Trading date         |
| index_name  | TEXT      | Benchmark index name |
| close_value | REAL      | Index closing value  |

---

# Data Quality Notes

### Missing Values

* monthly_sip_inflows.yoy_growth_pct contains 12 NULL values.
* These are expected because Year-over-Year growth cannot be calculated during the first year of observations.

### Date Standardization

The following fields were converted to datetime format:

* launch_date
* date
* month
* transaction_date
* portfolio_date

### Validation Rules Applied

* NAV > 0
* AUM > 0
* Expense Ratio between valid limits
* Transaction Amount > 0
* Weight Percentage between 0 and 100
* KYC Status validation
* Duplicate removal
* Date format standardization

### Overall Data Quality Assessment

**Quality Score:** 96 / 100

The datasets are clean, consistent, and suitable for SQL analytics, dashboard development, reporting, and machine learning workflows.
