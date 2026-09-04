import pandas as pd
from pathlib import Path

# --------------------------------------------------
# Project paths
# --------------------------------------------------

RAW_DATA_DIR = Path("data/raw")

# --------------------------------------------------
# Dataset files
# --------------------------------------------------

datasets = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

# --------------------------------------------------
# Load and inspect all datasets
# --------------------------------------------------

dataframes = {}

print("=" * 70)
print("DAY 1 - DATA INGESTION")
print("=" * 70)

for filename in datasets:

    file_path = RAW_DATA_DIR / filename

    print("\n" + "=" * 70)
    print(f"DATASET: {filename}")
    print("=" * 70)

    try:
        df = pd.read_csv(file_path)

        dataframes[filename] = df

        # Shape
        print("\nShape:")
        print(df.shape)

        # Data types
        print("\nData Types:")
        print(df.dtypes)

        # First 5 rows
        print("\nFirst 5 Rows:")
        print(df.head())

        # Missing values
        print("\nMissing Values:")
        print(df.isnull().sum())

        # Duplicate rows
        print("\nDuplicate Rows:")
        print(df.duplicated().sum())

    except FileNotFoundError:
        print(f"ERROR: {filename} was not found in data/raw")

    except Exception as e:
        print(f"ERROR loading {filename}: {e}")


# --------------------------------------------------
# Explore Fund Master
# --------------------------------------------------

print("\n" + "=" * 70)
print("FUND MASTER EXPLORATION")
print("=" * 70)

fund_master = dataframes.get("01_fund_master.csv")

if fund_master is not None:

    print("\nColumns in Fund Master:")
    print(fund_master.columns.tolist())

    # Unique Fund Houses
    if "fund_house" in fund_master.columns:
        print("\nUnique Fund Houses:")
        print(fund_master["fund_house"].unique())

    # Unique Categories
    if "category" in fund_master.columns:
        print("\nUnique Categories:")
        print(fund_master["category"].unique())

    # Unique Sub-Categories
    if "sub_category" in fund_master.columns:
        print("\nUnique Sub-Categories:")
        print(fund_master["sub_category"].unique())

    # Unique Risk Grades
    if "risk_category" in fund_master.columns:
        print("\nUnique Risk Grades:")
        print(fund_master["risk_category"].unique())


# --------------------------------------------------
# Validate AMFI Codes
# --------------------------------------------------

print("\n" + "=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

nav_history = dataframes.get("02_nav_history.csv")

if fund_master is not None and nav_history is not None:

    print("\nFund Master columns:")
    print(fund_master.columns.tolist())

    print("\nNAV History columns:")
    print(nav_history.columns.tolist())

    if "amfi_code" in fund_master.columns and "amfi_code" in nav_history.columns:

        fund_codes = set(
            fund_master["amfi_code"]
            .dropna()
            .astype(str)
            .str.strip()
        )

        nav_codes = set(
            nav_history["amfi_code"]
            .dropna()
            .astype(str)
            .str.strip()
        )

        missing_codes = fund_codes - nav_codes

        print(f"\nUnique AMFI codes in Fund Master: {len(fund_codes)}")
        print(f"Unique AMFI codes in NAV History: {len(nav_codes)}")
        print(f"AMFI codes missing from NAV History: {len(missing_codes)}")

        if missing_codes:
            print("\nMissing AMFI Codes:")
            print(sorted(missing_codes))
        else:
            print("\nSUCCESS: Every AMFI code in Fund Master exists in NAV History.")

    else:
        print("\nWARNING: 'amfi_code' column not found in one or both datasets.")


# --------------------------------------------------
# Data Quality Summary
# --------------------------------------------------

print("\n" + "=" * 70)
print("DATA QUALITY SUMMARY")
print("=" * 70)

for filename, df in dataframes.items():

    missing = df.isnull().sum().sum()
    duplicates = df.duplicated().sum()

    print(
        f"{filename}: "
        f"{len(df)} rows, "
        f"{len(df.columns)} columns, "
        f"{missing} missing values, "
        f"{duplicates} duplicate rows"
    )

print("\nDay 1 data ingestion inspection complete.")