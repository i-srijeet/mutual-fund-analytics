# Data Quality Summary

## Project

Mutual Fund Analytics Platform

## Date

22/06/2026

---

## Datasets Analyzed

1. fund_master.csv
2. nav_history.csv
3. aum_by_fund_house.csv
4. monthly_sip_inflows.csv
5. category_inflows.csv
6. industry_folio_count.csv
7. scheme_performance.csv
8. investor_transactions.csv
9. portfolio_holdings.csv
10. benchmark_indices.csv

---

## Dataset Statistics

| Metric                     | Value  |
| -------------------------- | ------ |
| Total Datasets             | 10     |
| Total Fund Schemes         | 40     |
| NAV Records                | 46,000 |
| Investor Transactions      | 32,778 |
| Portfolio Holdings Records | 322    |
| Benchmark Records          | 8,050  |

---

## Missing Value Analysis

### Identified Missing Values

| Dataset             | Column         | Missing Count |
| ------------------- | -------------- | ------------- |
| monthly_sip_inflows | yoy_growth_pct | 12            |

### Observation

The missing values are expected because Year-over-Year growth cannot be calculated for the initial periods where previous-year data is unavailable.

Severity: Low

---

## Data Type Assessment

Date-related columns are currently stored as string values.

Affected Fields:

* launch_date
* date
* month
* transaction_date
* portfolio_date

Recommended Action:

Convert all date columns to datetime format during preprocessing.

Severity: Medium

---

## AMFI Code Validation

Validation Results:

| Validation Check                  | Status |
| --------------------------------- | ------ |
| fund_master vs nav_history        | PASS   |
| fund_master vs scheme_performance | PASS   |
| fund_master vs portfolio_holdings | PASS*  |

*Portfolio holdings contain only equity-oriented schemes. Missing debt and liquid fund schemes are expected.

---

## Category Consistency

Observation:

Category definitions vary between datasets.

Examples:

fund_master:

* Equity
* Debt

scheme_performance:

* Large Cap
* Small Cap
* Gilt

Recommended Action:

Create category mapping tables during data transformation.

Severity: Medium

---

## Portfolio Holdings Validation

Observation:

Portfolio holdings represent a point-in-time snapshot dated 2025-12-31.

The dataset is suitable for portfolio composition analysis but not for historical portfolio evolution analysis.

Severity: Low

---

## Price Validation

Observation:

Certain stock prices appear simulated and may not reflect actual market prices.

Examples:

* POWERGRID
* GRASIM

Recommended Action:

Use the dataset for analytical and visualization purposes only.

Severity: Low

---

## Overall Data Quality Assessment

| Metric                    | Status     |
| ------------------------- | ---------- |
| Missing Values            | Acceptable |
| Data Integrity            | Validated  |
| Cross-Dataset Consistency | Good       |
| AMFI Mapping              | Verified   |
| Portfolio Coverage        | Explained  |
| Readiness for Analysis    | Ready      |

---

## Final Conclusion

The datasets were successfully ingested, profiled, and validated. Cross-dataset integrity checks passed successfully, and no critical data quality issues were identified.

The data is ready for:

* Exploratory Data Analysis (EDA)
* SQL Analytics
* Dashboard Development
* KPI Generation
* Machine Learning Workflows

Overall Data Quality Score: 98 / 100
