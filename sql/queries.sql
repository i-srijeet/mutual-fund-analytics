-- 1. Top 5 Funds by AUM

SELECT
    scheme_name,
    aum_crore
FROM scheme_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- 2. Average NAV by Fund

SELECT
    amfi_code,
    ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY amfi_code
ORDER BY avg_nav DESC;


-- 3. Monthly Average NAV

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav),2) AS avg_nav
FROM nav_history
GROUP BY month
ORDER BY month;


-- 4. SIP Year-over-Year Growth

SELECT
    month,
    yoy_growth_pct
FROM monthly_sip_inflows
ORDER BY month;


-- 5. Transactions by State

SELECT
    state,
    COUNT(*) AS total_transactions
FROM investor_transactions
GROUP BY state
ORDER BY total_transactions DESC;


-- 6. Funds with Expense Ratio < 1%

SELECT
    scheme_name,
    expense_ratio_pct
FROM scheme_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;


-- 7. Top Performing Funds (5 Year Return)

SELECT
    scheme_name,
    return_5yr_pct
FROM scheme_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;


-- 8. Fund House Wise AUM

SELECT
    fund_house,
    ROUND(SUM(aum_crore),2) AS total_aum
FROM aum_by_fund_house
GROUP BY fund_house
ORDER BY total_aum DESC;


-- 9. KYC Status Distribution

SELECT
    kyc_status,
    COUNT(*) AS investors
FROM investor_transactions
GROUP BY kyc_status;


-- 10. Benchmark Performance Overview

SELECT
    index_name,
    ROUND(AVG(close_value),2) AS avg_index_value
FROM benchmark_indices
GROUP BY index_name
ORDER BY avg_index_value DESC;