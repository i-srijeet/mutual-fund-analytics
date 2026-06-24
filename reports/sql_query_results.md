# SQL Query Results Report

## Project

**Mutual Fund Analytics Platform**

## Date

24 June 2026

---

# Query 1: Top 5 Funds by AUM

### SQL

```sql
SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;
```

### Result Summary

| Rank | Scheme Name                        | AUM (Crore) |
| ---- | ---------------------------------- | ----------: |
| 1    | Mirae Asset Emerging Bluechip Fund |      49,046 |
| 2    | Kotak Emerging Equity Fund         |      47,469 |
| 3    | Nippon India Small Cap Fund        |      43,630 |
| 4    | DSP Top 100 Equity Fund            |      41,828 |
| 5    | UTI Mid Cap Fund                   |      41,728 |

### Observation

Mirae Asset Emerging Bluechip Fund has the highest Assets Under Management (AUM) among all analyzed schemes. Small-cap and mid-cap oriented funds dominate the top positions, indicating strong investor participation in growth-oriented equity funds.

---

# Query 2: Average NAV Per Month

### SQL

```sql
SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;
```

### Observation

The average NAV increased steadily from **207.06 in January 2022** to **357.04 in May 2026**, indicating sustained long-term growth across the mutual fund universe.

### Key Insight

Average NAV grew by approximately **72.4%** during the analysis period, reflecting positive market performance and wealth creation.

---

# Query 3: SIP Year-over-Year Growth

### SQL

```sql
SELECT
    month,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;
```

### Observation

The first 12 months contain NULL values because prior-year comparison data was unavailable.

### Key Insight

SIP growth accelerated significantly during 2024, reaching a peak of approximately **53.05% YoY**, demonstrating strong retail investor participation in mutual funds.

---

# Query 4: Transactions by State

### SQL

```sql
SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;
```

### Top States

| State          | Transactions |
| -------------- | -----------: |
| Punjab         |        2,965 |
| Madhya Pradesh |        2,931 |
| Tamil Nadu     |        2,806 |
| Gujarat        |        2,780 |
| West Bengal    |        2,748 |

### Observation

Punjab recorded the highest number of transactions, closely followed by Madhya Pradesh and Tamil Nadu. Transaction distribution appears balanced across major Indian states.

---

# Query 5: Funds with Expense Ratio Below 1%

### SQL

```sql
SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;
```

### Observation

Fourteen schemes were identified with expense ratios below 1%.

### Key Insight

Debt funds, liquid funds, index funds, and direct plans generally offer the lowest expense ratios, making them cost-efficient investment options.

---

# Query 6: Top 10 Funds by 5-Year Return

### SQL

```sql
SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;
```

### Top Performer

| Scheme              | 5-Year Return (%) |
| ------------------- | ----------------: |
| ABSL Small Cap Fund |             23.80 |

### Observation

Small-cap funds dominate the top-performing category, delivering returns above 20% over the five-year period.

### Key Insight

Higher-return schemes are associated with higher risk categories, illustrating the risk-return tradeoff in equity investing.

---

# Query 7: Fund House Wise Total AUM

### SQL

```sql
SELECT
    fund_house,
    SUM(aum_crore) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;
```

### Top Fund Houses

| Fund House          | Total AUM |
| ------------------- | --------: |
| SBI Mutual Fund     | 8,491,000 |
| ICICI Prudential MF | 6,293,000 |
| HDFC Mutual Fund    | 5,732,000 |

### Observation

SBI Mutual Fund leads the industry by total AUM, followed by ICICI Prudential and HDFC Mutual Fund.

---

# Query 8: KYC Status Distribution

### SQL

```sql
SELECT
    kyc_status,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY kyc_status;
```

### Result

| KYC Status | Investors |
| ---------- | --------: |
| Verified   |    30,146 |
| Pending    |     2,632 |

### Observation

Approximately 92% of investors have completed KYC verification.

### Key Insight

The investor base demonstrates a high level of regulatory compliance.

---

# Query 9: Benchmark Average Index Value

### SQL

```sql
SELECT
    index_name,
    ROUND(AVG(close_value),2) AS avg_index
FROM benchmark_indices
GROUP BY index_name
ORDER BY avg_index DESC;
```

### Observation

BSE Small Cap recorded the highest average index value among benchmark indices.

### Ranking

1. BSE Small Cap
2. NIFTY 500
3. NIFTY 50
4. NIFTY Midcap 150
5. NIFTY 100

### Key Insight

Broader market and small-cap indices generated stronger performance relative to traditional large-cap benchmarks.

---

# Query 10: Transaction Type Distribution

### SQL

```sql
SELECT
    transaction_type,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY transaction_type
ORDER BY total_transactions DESC;
```

### Result

| Transaction Type |  Count |
| ---------------- | -----: |
| SIP              | 19,716 |
| Lumpsum          |  8,095 |
| Redemption       |  4,967 |

### Observation

Systematic Investment Plans (SIPs) account for the majority of transactions.

### Key Insight

Retail investors increasingly prefer disciplined periodic investing over one-time investments.

---

# Overall Business Insights

1. Mutual fund industry assets are concentrated among a few large fund houses led by SBI Mutual Fund.
2. Average NAV demonstrates a strong long-term upward trend across schemes.
3. SIP participation continues to grow rapidly, highlighting increasing retail investor engagement.
4. Small-cap funds generated the highest historical returns but are associated with higher risk.
5. Most investors are KYC compliant, supporting regulatory readiness.
6. SIP transactions dominate investor activity, confirming the popularity of systematic investing.
7. Low-expense direct plans and passive products offer cost advantages for investors.
8. Small-cap benchmark indices outperformed broader market benchmarks during the analysis period.

---

## Conclusion

The SQL analytics layer successfully extracted meaningful business insights from the Mutual Fund Analytics Platform. All ten analytical queries executed successfully against the SQLite database, validating the ETL pipeline, database design, and reporting framework developed during Day 2.
