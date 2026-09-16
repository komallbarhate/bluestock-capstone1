import pandas as pd
from pathlib import Path


# Project paths
PROJECT_ROOT = Path(__file__).resolve().parent
DATA_PATH = PROJECT_ROOT / "data" / "processed"


# Load fund data
fund_master = pd.read_csv(
    DATA_PATH / "01_fund_master_cleaned.csv"
)

performance = pd.read_csv(
    DATA_PATH / "07_scheme_performance_cleaned.csv"
)


# Merge fund information with performance metrics
funds = fund_master[
    ["amfi_code", "scheme_name", "fund_house", "risk_category"]
].merge(
    performance[
        ["amfi_code", "sharpe_ratio"]
    ],
    on="amfi_code",
    how="inner"
)


def recommend_funds(risk_appetite):
    """
    Return top 3 funds by Sharpe ratio
    within the matching risk category.
    """

    risk_appetite = risk_appetite.strip().title()

    valid_risk_categories = ["Low", "Moderate", "High"]

    if risk_appetite not in valid_risk_categories:
        print("Please enter: Low, Moderate, or High")
        return

    recommendations = funds[
        funds["risk_category"] == risk_appetite
    ].sort_values(
        "sharpe_ratio",
        ascending=False
    ).head(3)

    print(f"\nTop 3 Funds for {risk_appetite} Risk Appetite")
    print("-" * 70)

    print(
        recommendations[
            [
                "amfi_code",
                "scheme_name",
                "fund_house",
                "risk_category",
                "sharpe_ratio"
            ]
        ].to_string(index=False)
    )


if __name__ == "__main__":

    print("Fund Recommendation System")
    print("Risk Appetite: Low / Moderate / High")

    risk = input("Enter risk appetite: ")

    recommend_funds(risk)