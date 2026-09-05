import pandas as pd
from sqlalchemy import create_engine, text
from pathlib import Path

# ==================================================
# SQLite Database Setup
# ==================================================

engine = create_engine("sqlite:///bluestock_mf.db")

processed_dir = Path("data/processed")

print("=" * 70)
print("LOADING BLUESTOCK MUTUAL FUND DATABASE")
print("=" * 70)


# ==================================================
# Load Dimension: dim_fund
# ==================================================

fund_master = pd.read_csv(
    processed_dir / "01_fund_master_cleaned.csv"
)

fund_master.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

print("dim_fund loaded:", len(fund_master), "rows")


# ==================================================
# Load Dimension: dim_date
# ==================================================

nav = pd.read_csv(
    processed_dir / "02_nav_history_cleaned.csv"
)

transactions = pd.read_csv(
    processed_dir / "08_investor_transactions_cleaned.csv"
)

aum = pd.read_csv(
    processed_dir / "03_aum_by_fund_house_cleaned.csv"
)

benchmarks = pd.read_csv(
    processed_dir / "10_benchmark_indices_cleaned.csv"
)

sip = pd.read_csv(
    processed_dir / "04_monthly_sip_inflows_cleaned.csv"
)

date_values = set()

date_values.update(nav["date"].astype(str))
date_values.update(transactions["transaction_date"].astype(str))
date_values.update(aum["date"].astype(str))
date_values.update(benchmarks["date"].astype(str))

dim_date = pd.DataFrame(
    {"date": sorted(date_values)}
)

dim_date.to_sql(
    "dim_date",
    engine,
    if_exists="replace",
    index=False
)

print("dim_date loaded:", len(dim_date), "rows")


# ==================================================
# Load Fact: fact_nav
# ==================================================

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

print("fact_nav loaded:", len(nav), "rows")


# ==================================================
# Load Fact: fact_transactions
# ==================================================

transactions.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

print("fact_transactions loaded:", len(transactions), "rows")


# ==================================================
# Load Fact: fact_performance
# ==================================================

performance = pd.read_csv(
    processed_dir / "07_scheme_performance_cleaned.csv"
)

performance.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("fact_performance loaded:", len(performance), "rows")


# ==================================================
# Load Fact: fact_aum
# ==================================================

aum.to_sql(
    "fact_aum",
    engine,
    if_exists="replace",
    index=False
)

print("fact_aum loaded:", len(aum), "rows")


# ==================================================
# Load SIP Inflows for Analytical Queries
# ==================================================

sip.to_sql(
    "sip_inflows",
    engine,
    if_exists="replace",
    index=False
)

print("sip_inflows loaded:", len(sip), "rows")


# ==================================================
# Verify Database Row Counts
# ==================================================

print("\n" + "=" * 70)
print("DATABASE ROW COUNT VERIFICATION")
print("=" * 70)

tables = [
    "dim_fund",
    "dim_date",
    "fact_nav",
    "fact_transactions",
    "fact_performance",
    "fact_aum",
    "sip_inflows"
]

for table in tables:

    with engine.connect() as connection:

        result = connection.execute(
            text(f"SELECT COUNT(*) FROM {table}")
        )

        count = result.scalar()

    print(f"{table}: {count} rows")


# ==================================================
# Database Complete
# ==================================================

print("\n" + "=" * 70)
print("DATABASE LOADING COMPLETE")
print("=" * 70)

print("Database saved as: bluestock_mf.db")