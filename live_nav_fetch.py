import requests
import pandas as pd
from pathlib import Path

# API scheme codes
schemes = {
    125497: "HDFC Top 100 Direct",
    119551: "SBI Bluechip",
    120503: "ICICI Bluechip",
    118632: "Nippon Large Cap",
    119092: "Axis Bluechip",
    120841: "Kotak Bluechip"
}

# Output folder
output_dir = Path("data/raw")
output_dir.mkdir(parents=True, exist_ok=True)

# Fetch NAV data
for scheme_code, scheme_label in schemes.items():

    print("\n" + "=" * 70)
    print(f"Fetching: {scheme_label}")
    print(f"Scheme Code: {scheme_code}")
    print("=" * 70)

    url = f"https://api.mfapi.in/mf/{scheme_code}"

    response = requests.get(url)
    response.raise_for_status()

    data = response.json()

    # Parse NAV data
    nav_data = pd.DataFrame(data["data"])

    # Add scheme information
    nav_data["scheme_code"] = data["meta"]["scheme_code"]
    nav_data["scheme_name"] = data["meta"]["scheme_name"]

    # Save CSV
    output_path = output_dir / f"{scheme_code}_nav.csv"
    nav_data.to_csv(output_path, index=False)

    print(f"API Scheme Name: {data['meta']['scheme_name']}")
    print(f"Records fetched: {len(nav_data)}")
    print(f"Saved to: {output_path}")