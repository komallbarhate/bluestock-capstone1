# Bluestock Mutual Fund Data Dictionary

## Project

Bluestock Mutual Fund Capstone Project

## Day 2: Data Cleaning + SQL Database Design

This document describes the columns, data types, business definitions, and source datasets used in the project.

---

# 1. fund_master

Source: `01_fund_master.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identification code |
| fund_house | TEXT | Name of the mutual fund house |
| scheme_name | TEXT | Name of the mutual fund scheme |
| category | TEXT | Broad mutual fund category |
| sub_category | TEXT | Detailed sub-category of the fund |
| plan | TEXT | Investment plan type |
| launch_date | DATE | Date on which the scheme was launched |
| benchmark | TEXT | Benchmark index used for performance comparison |
| expense_ratio_pct | REAL | Annual expense ratio of the scheme in percentage |
| exit_load_pct | REAL | Exit load applicable to the scheme in percentage |
| min_sip_amount | REAL | Minimum amount required for SIP investment |
| min_lumpsum_amount | REAL | Minimum amount required for lumpsum investment |
| fund_manager | TEXT | Fund manager responsible for the scheme |
| risk_category | TEXT | Risk classification of the scheme |
| sebi_category_code | TEXT | SEBI category classification code |

---

# 2. nav_history

Source: `02_nav_history.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identification code |
| date | DATE | Date of NAV observation |
| nav | REAL | Net Asset Value of the mutual fund scheme |

Cleaning performed:
- Converted date to datetime
- Sorted by AMFI code and date
- Forward-filled missing NAV values
- Removed duplicate records
- Validated NAV values greater than zero

---

# 3. aum_by_fund_house

Source: `03_aum_by_fund_house.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| date | DATE | Date of AUM measurement |
| fund_house | TEXT | Name of the mutual fund house |
| aum_lakh_crore | REAL | Assets under management measured in lakh crore |
| aum_crore | REAL | Assets under management measured in crore |
| num_schemes | INTEGER | Number of schemes managed by the fund house |

---

# 4. monthly_sip_inflows

Source: `04_monthly_sip_inflows.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| month | DATE/TEXT | Month of SIP activity |
| sip_inflow_crore | REAL | SIP inflow amount in crore |
| active_sip_accounts_crore | REAL | Number of active SIP accounts in crore |
| new_sip_accounts_lakh | REAL | Number of new SIP accounts in lakh |
| sip_aum_lakh_crore | REAL | SIP assets under management in lakh crore |
| yoy_growth_pct | REAL | Year-over-year SIP growth percentage |

---

# 5. category_inflows

Source: `05_category_inflows.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| month | DATE/TEXT | Month of the recorded inflow |
| category | TEXT | Mutual fund category |
| net_inflow_crore | REAL | Net inflow into the category in crore |

---

# 6. industry_folio_count

Source: `06_industry_folio_count.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| month | DATE/TEXT | Month of folio measurement |
| total_folios_crore | REAL | Total mutual fund folios in crore |
| equity_folios_crore | REAL | Equity fund folios in crore |
| debt_folios_crore | REAL | Debt fund folios in crore |
| hybrid_folios_crore | REAL | Hybrid fund folios in crore |
| others_folios_crore | REAL | Other category folios in crore |

---

# 7. scheme_performance

Source: `07_scheme_performance.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| amfi_code | INTEGER | Unique AMFI scheme identification code |
| scheme_name | TEXT | Name of the mutual fund scheme |
| fund_house | TEXT | Name of the mutual fund house |
| category | TEXT | Mutual fund category |
| plan | TEXT | Investment plan type |
| return_1yr_pct | REAL | One-year return percentage |
| return_3yr_pct | REAL | Three-year return percentage |
| return_5yr_pct | REAL | Five-year return percentage |
| benchmark_3yr_pct | REAL | Three-year benchmark return percentage |
| alpha | REAL | Excess return relative to the benchmark |
| beta | REAL | Sensitivity of fund returns to market movements |
| sharpe_ratio | REAL | Risk-adjusted return measure using total risk |
| sortino_ratio | REAL | Risk-adjusted return measure using downside risk |
| std_dev_ann_pct | REAL | Annualized standard deviation percentage |
| max_drawdown_pct | REAL | Maximum observed percentage decline |
| aum_crore | INTEGER | Assets under management in crore |
| expense_ratio_pct | REAL | Annual expense ratio in percentage |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Risk classification grade |

Cleaning performed:
- Validated return values as numeric
- Checked for return value anomalies
- Validated expense ratio range of 0.1% to 2.5%

---

# 8. investor_transactions

Source: `08_investor_transactions.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| investor_id | TEXT | Unique investor identifier |
| transaction_date | DATE | Date of transaction |
| amfi_code | INTEGER | AMFI scheme identification code |
| transaction_type | TEXT | Type of transaction: SIP, Lumpsum, or Redemption |
| amount_inr | INTEGER | Transaction amount in Indian Rupees |
| state | TEXT | Investor's state |
| city | TEXT | Investor's city |
| city_tier | TEXT | Classification of the investor's city |
| age_group | TEXT | Age group of the investor |
| gender | TEXT | Gender of the investor |
| annual_income_lakh | REAL | Annual income in lakh |
| payment_mode | TEXT | Mode used for payment |
| kyc_status | TEXT | KYC status: Verified or Pending |

Cleaning performed:
- Standardised transaction type values
- Validated transaction amount greater than zero
- Converted transaction date to datetime
- Validated KYC status values

---

# 9. portfolio_holdings

Source: `09_portfolio_holdings.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| amfi_code | INTEGER | AMFI scheme identification code |
| stock_symbol | TEXT | Stock market symbol |
| stock_name | TEXT | Name of the stock |
| sector | TEXT | Sector in which the stock operates |
| weight_pct | REAL | Stock weight in the portfolio percentage |
| market_value_cr | REAL | Market value of holding in crore |
| current_price_inr | REAL | Current stock price in Indian Rupees |
| portfolio_date | DATE | Date of portfolio holding |

---

# 10. benchmark_indices

Source: `10_benchmark_indices.csv`

| Column | Data Type | Business Definition |
|---|---|---|
| date | DATE | Date of index observation |
| index_name | TEXT | Name of benchmark index |
| close_value | REAL | Closing value of the benchmark index |

---

# SQLite Database Tables

Database: `bluestock_mf.db`

| Table | Type | Source |
|---|---|---|
| dim_fund | Dimension | 01_fund_master.csv |
| dim_date | Dimension | Date values from project datasets |
| fact_nav | Fact | 02_nav_history.csv |
| fact_transactions | Fact | 08_investor_transactions.csv |
| fact_performance | Fact | 07_scheme_performance.csv |
| fact_aum | Fact | 03_aum_by_fund_house.csv |
| sip_inflows | Analytical table | 04_monthly_sip_inflows.csv |

---

# Data Quality Summary

## NAV History

- Original rows: 46,000
- Invalid NAV values: 0
- Duplicate records: 0
- NAV validation: Passed

## Investor Transactions

- Original rows: 32,778
- Invalid transaction types: 0
- Invalid transaction amounts: 0
- Invalid KYC status values: 0
- Duplicate records: 0
- Missing values: 0

## Scheme Performance

- Original rows: 40
- Non-numeric return values: 0
- Return anomalies: 0
- Expense ratios outside 0.1%–2.5%: 0
- Duplicate records: 0
- Missing values: 0

---

# Source References

The data dictionary definitions are based on the provided CSV datasets used in the Bluestock Mutual Fund Capstone Project.

The SQLite database was created using SQLAlchemy and Pandas `to_sql()`.