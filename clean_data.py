import pandas as pd
from pathlib import Path

# Create processed folder
processed_dir = Path("data/processed")
processed_dir.mkdir(parents=True, exist_ok=True)


# ==================================================
# Task 1: Clean nav_history.csv
# ==================================================

input_path = Path("data/raw/02_nav_history.csv")
output_path = processed_dir / "02_nav_history_cleaned.csv"

df = pd.read_csv(input_path)

print("=" * 70)
print("CLEANING NAV HISTORY")
print("=" * 70)

print("Original shape:", df.shape)

# Parse dates to datetime
df["date"] = pd.to_datetime(df["date"])

# Sort by AMFI code + date
df = df.sort_values(["amfi_code", "date"])

# Forward-fill missing NAV
df["nav"] = df.groupby("amfi_code")["nav"].ffill()

# Remove duplicates
df = df.drop_duplicates()

# Validate NAV > 0
invalid_nav = (df["nav"] <= 0).sum()

print("Invalid NAV values (<= 0):", invalid_nav)

if invalid_nav > 0:
    print("WARNING: NAV values <= 0 found.")
else:
    print("Validation passed: All NAV values are greater than 0.")

df.to_csv(output_path, index=False)

print("Cleaned shape:", df.shape)
print("Saved to:", output_path)


# ==================================================
# Task 2: Clean investor_transactions.csv
# ==================================================

input_path = Path("data/raw/08_investor_transactions.csv")
output_path = processed_dir / "08_investor_transactions_cleaned.csv"

transactions = pd.read_csv(input_path)

print("\n" + "=" * 70)
print("CLEANING INVESTOR TRANSACTIONS")
print("=" * 70)

print("Original shape:", transactions.shape)

# Standardise transaction_type values
transactions["transaction_type"] = (
    transactions["transaction_type"]
    .str.strip()
)

valid_transaction_types = [
    "SIP",
    "Lumpsum",
    "Redemption"
]

invalid_transaction_types = (
    ~transactions["transaction_type"].isin(valid_transaction_types)
).sum()

print("Invalid transaction types:", invalid_transaction_types)

# Validate amount > 0
invalid_amounts = (transactions["amount_inr"] <= 0).sum()

print("Invalid amounts (<= 0):", invalid_amounts)

# Fix date format
transactions["transaction_date"] = pd.to_datetime(
    transactions["transaction_date"]
)

# Check KYC status enum values
valid_kyc_status = [
    "Verified",
    "Pending"
]

invalid_kyc = (
    ~transactions["kyc_status"].isin(valid_kyc_status)
).sum()

print("Invalid KYC status values:", invalid_kyc)

transactions.to_csv(output_path, index=False)

print("Cleaned shape:", transactions.shape)
print("Saved to:", output_path)


# ==================================================
# Task 3: Clean scheme_performance.csv
# ==================================================

input_path = Path("data/raw/07_scheme_performance.csv")
output_path = processed_dir / "07_scheme_performance_cleaned.csv"

performance = pd.read_csv(input_path)

print("\n" + "=" * 70)
print("CLEANING SCHEME PERFORMANCE")
print("=" * 70)

print("Original shape:", performance.shape)

# Return columns
return_columns = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct"
]

# Validate return values are numeric
invalid_return_values = 0

for column in return_columns:
    numeric_values = pd.to_numeric(
        performance[column],
        errors="coerce"
    )

    invalid_return_values += numeric_values.isna().sum()

    performance[column] = numeric_values

print("Invalid/non-numeric return values:", invalid_return_values)

# Flag anomalies
anomaly_count = 0

for column in return_columns:
    anomaly_count += performance[column].isna().sum()

print("Return value anomalies:", anomaly_count)

# Check expense ratio range
expense_ratio_invalid = (
    (performance["expense_ratio_pct"] < 0.1) |
    (performance["expense_ratio_pct"] > 2.5)
).sum()

print(
    "Expense ratios outside 0.1%-2.5%:",
    expense_ratio_invalid
)

if expense_ratio_invalid > 0:
    print("WARNING: Expense ratio anomalies found.")
else:
    print(
        "Validation passed: All expense ratios are "
        "within 0.1%-2.5%."
    )

performance.to_csv(output_path, index=False)

print("Cleaned shape:", performance.shape)
print("Saved to:", output_path)


# ==================================================
# Remaining 7 datasets
# Preserve source data and save to processed folder
# ==================================================

remaining_files = [
    "01_fund_master.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("\n" + "=" * 70)
print("PROCESSING REMAINING DATASETS")
print("=" * 70)

for filename in remaining_files:

    input_path = Path("data/raw") / filename
    output_path = processed_dir / filename.replace(
        ".csv",
        "_cleaned.csv"
    )

    data = pd.read_csv(input_path)

    data.to_csv(output_path, index=False)

    print(f"{filename}: {data.shape} -> {output_path}")