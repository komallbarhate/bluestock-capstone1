-- ============================================================
-- Bluestock Mutual Fund Capstone
-- Day 2: 10 Analytical SQL Queries
-- ============================================================


-- ============================================================
-- 1. Top 5 Funds by AUM
-- ============================================================

SELECT
    amfi_code,
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;


-- ============================================================
-- 2. Average NAV per Month
-- ============================================================

SELECT
    strftime('%Y-%m', date) AS month,
    ROUND(AVG(nav), 4) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', date)
ORDER BY month;


-- ============================================================
-- 3. SIP Year-over-Year Growth
-- ============================================================

SELECT
    month,
    sip_inflow_crore,
    active_sip_accounts_crore,
    new_sip_accounts_lakh,
    sip_aum_lakh_crore,
    yoy_growth_pct
FROM sip_inflows
ORDER BY month;


-- ============================================================
-- 4. Transactions by State
-- ============================================================

SELECT
    state,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_transaction_amount
FROM fact_transactions
GROUP BY state
ORDER BY total_transaction_amount DESC;


-- ============================================================
-- 5. Funds with Expense Ratio Less Than 1%
-- ============================================================

SELECT
    amfi_code,
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1.0
ORDER BY expense_ratio_pct ASC;


-- ============================================================
-- 6. Transaction Count by Transaction Type
-- ============================================================

SELECT
    transaction_type,
    COUNT(*) AS transaction_count,
    ROUND(SUM(amount_inr), 2) AS total_amount
FROM fact_transactions
GROUP BY transaction_type
ORDER BY transaction_count DESC;


-- ============================================================
-- 7. Top 10 Funds by 1-Year Return
-- ============================================================

SELECT
    amfi_code,
    scheme_name,
    fund_house,
    return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 10;


-- ============================================================
-- 8. Funds with Positive Alpha
-- ============================================================

SELECT
    amfi_code,
    scheme_name,
    fund_house,
    alpha
FROM fact_performance
WHERE alpha > 0
ORDER BY alpha DESC;


-- ============================================================
-- 9. AUM by Fund House
-- ============================================================

SELECT
    fund_house,
    ROUND(SUM(aum_crore), 2) AS total_aum_crore,
    SUM(num_schemes) AS total_schemes
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum_crore DESC;


-- ============================================================
-- 10. Average Transaction Amount by KYC Status
-- ============================================================

SELECT
    kyc_status,
    COUNT(*) AS transaction_count,
    ROUND(AVG(amount_inr), 2) AS average_transaction_amount
FROM fact_transactions
GROUP BY kyc_status
ORDER BY average_transaction_amount DESC;