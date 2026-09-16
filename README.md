# Bluestock Mutual Fund Analytics

## Project Overview

This project analyzes mutual fund data to understand fund performance, investor behavior, SIP trends, AUM growth, and market trends.

The project combines data cleaning, exploratory data analysis, SQL database design, financial performance analytics, and an interactive Power BI dashboard.

## Objectives

- Clean and validate mutual fund datasets.
- Design and populate a SQLite database.
- Analyze NAV and fund performance.
- Calculate CAGR, Sharpe Ratio, Sortino Ratio, Alpha, Beta, and Maximum Drawdown.
- Create a composite fund scorecard.
- Analyze SIP inflows, AUM, folios, and investor transactions.
- Study investor demographics and geographic patterns.
- Compare fund performance with market benchmarks.
- Build an interactive Power BI dashboard.

## Project Structure

```text
capstone project/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   ├── EDA_Analysis.ipynb
│   └── EDA visualizations
│
├── sql/
│
├── reports/
│
├── Performance_Analytics.ipynb
├── fund_scorecard.csv
├── alpha_beta.csv
├── tracking_error.csv
├── benchmark_comparison.png
├── bluestock_mf.db
│
├── clean_data.py
├── data_ingestion.py
├── live_nav_fetch.py
├── load_database.py
├── queries.sql
├── schema.sql
├── data_dictionary.md
├── requirements.txt
└── bluestock_mf_dashboard.pbix


Dataset

The project uses multiple mutual fund datasets covering:

Fund master information
Historical NAV
AUM by fund house
Monthly SIP inflows
Category-wise inflows
Industry folio counts
Investor transactions
Portfolio holdings
Benchmark index data
Scheme performance
Data Cleaning

The datasets were cleaned using Python with Pandas and NumPy.

The cleaning process includes:

Handling missing values
Standardizing data types
Validating AMFI scheme codes
Validating NAV values
Validating transaction types
Validating KYC status
Checking expense ratio ranges
Removing inconsistencies and preparing processed datasets
SQL Database

A SQLite database was designed to organize the cleaned mutual fund data.

Database:

bluestock_mf.db

SQL files include:

schema.sql
queries.sql
Exploratory Data Analysis

EDA was performed using Python, Pandas, Matplotlib, Seaborn, and Plotly.

Key analyses include:

NAV trends across 40 schemes
AUM growth by fund house
Monthly SIP inflows
Category-wise inflow analysis
Investor age distribution
Investor gender distribution
SIP amount by age group
SIP amount by state
T30 vs B30 analysis
Folio growth
NAV return correlation
Sector allocation
Transaction type distribution
Payment mode distribution
Performance Analytics

Fund performance was evaluated using:

Daily returns
1-year CAGR
3-year CAGR
5-year CAGR
Sharpe Ratio
Sortino Ratio
Alpha
Beta
R-squared
Maximum Drawdown
Tracking Error

A composite Fund Score (0–100) was created using weighted performance and risk metrics.

Power BI Dashboard

An interactive Power BI dashboard was developed with the following pages:

1. Industry Overview
Total AUM
SIP inflows
Total folios
Total schemes
Industry AUM trend
AUM by fund house
2. Fund Performance
3-Year Return vs Risk-Adjusted Performance
Fund scorecard
NAV and benchmark analysis
Fund House and Category slicers
Fund drill-through
3. Investor Analytics
Transaction amount by state
Transaction amount by transaction type
Average transaction amount by age group
Monthly transaction volume
State, Age Group, and City Tier slicers
4. SIP & Market Trends
Monthly SIP inflows
NIFTY 50 market trend
Category inflow heatmap
FY25 category inflow analysis
Category slicer
Technologies Used
Python
Pandas
NumPy
Matplotlib
Seaborn
Plotly
SciPy
SQLite
SQL
Jupyter Notebook
Power BI
Git
GitHub
Key Deliverables
Cleaned mutual fund datasets
SQLite database
EDA notebook and visualizations
Performance Analytics notebook
Fund Scorecard
Alpha/Beta analysis
Tracking Error analysis
Benchmark comparison
Interactive Power BI dashboard
Repository

This repository contains the data processing scripts, cleaned datasets, analytical notebooks, SQL database design, financial analysis outputs, and Power BI dashboard created for the Bluestock mutual fund analytics capstone project.