import requests
import pandas as pd
import os


scheme_codes = {
    "SBI_Bluechip": 119551,
    "ICICI_Bluechip": 120503,
    "Nippon_LargeCap": 118632,
    "Axis_Bluechip": 119092,
    "Kotak_Bluechip": 120841
}

for fund_name, amfi_code in scheme_codes.items():

    print(f"\nFetching {fund_name}...")

    url = f"https://api.mfapi.in/mf/{amfi_code}"

    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()

        nav_df = pd.DataFrame(data["data"])

        output_file = f"../data/raw/{fund_name}_NAV.csv"

        nav_df.to_csv(
            output_file,
            index=False
        )

        print(f"Saved -> {output_file}")

    else:
        print(f"Failed for {fund_name}")