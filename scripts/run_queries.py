import sqlite3
import pandas as pd

# Connect Database
conn = sqlite3.connect("bluestock_mf.db")

queries = {

    "1. Top 5 Funds by AUM": """
    SELECT
        scheme_name,
        aum_crore
    FROM scheme_performance
    ORDER BY aum_crore DESC
    LIMIT 5;
    """,

    "2. Average NAV Per Month": """
    SELECT
        strftime('%Y-%m', date) AS month,
        ROUND(AVG(nav),2) AS avg_nav
    FROM nav_history
    GROUP BY month
    ORDER BY month;
    """,

    "3. SIP YoY Growth": """
    SELECT
        month,
        yoy_growth_pct
    FROM monthly_sip_inflows
    ORDER BY month;
    """,

    "4. Transactions by State": """
    SELECT
        state,
        COUNT(*) AS total_transactions
    FROM investor_transactions
    GROUP BY state
    ORDER BY total_transactions DESC;
    """,

    "5. Funds with Expense Ratio < 1%": """
    SELECT
        scheme_name,
        expense_ratio_pct
    FROM scheme_performance
    WHERE expense_ratio_pct < 1
    ORDER BY expense_ratio_pct;
    """,

    "6. Top 10 Funds by 5 Year Return": """
    SELECT
        scheme_name,
        return_5yr_pct
    FROM scheme_performance
    ORDER BY return_5yr_pct DESC
    LIMIT 10;
    """,

    "7. Fund House Wise Total AUM": """
    SELECT
        fund_house,
        ROUND(SUM(aum_crore),2) AS total_aum
    FROM aum_by_fund_house
    GROUP BY fund_house
    ORDER BY total_aum DESC;
    """,

    "8. KYC Status Distribution": """
    SELECT
        kyc_status,
        COUNT(*) AS investors
    FROM investor_transactions
    GROUP BY kyc_status;
    """,

    "9. Benchmark Average Index Value": """
    SELECT
        index_name,
        ROUND(AVG(close_value),2) AS avg_index
    FROM benchmark_indices
    GROUP BY index_name
    ORDER BY avg_index DESC;
    """,

    "10. Transaction Type Distribution": """
    SELECT
        transaction_type,
        COUNT(*) AS total_transactions
    FROM investor_transactions
    GROUP BY transaction_type
    ORDER BY total_transactions DESC;
    """
}

for title, query in queries.items():

    print("\n")
    print("=" * 70)
    print(title)
    print("=" * 70)

    result = pd.read_sql(query, conn)

    print(result)

conn.close()

print("\n")
print("=" * 70)
print("ALL 10 SQL QUERIES EXECUTED SUCCESSFULLY")
print("=" * 70)