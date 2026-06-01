import pandas as pd


def get_climate_summary(location: str) -> dict:
    df = pd.read_csv("data/sample/bhutan_climate_summary.csv")

    row = df[df["district"].str.lower() == location.lower()]

    if row.empty:
        return {
            "location": location,
            "error": "Location not found in prototype climate database."
        }

    r = row.iloc[0]

    return {
        "location": r["district"],
        "annual_rainfall_mm": float(r["annual_rainfall_mm"]),
        "mean_temp_c": float(r["mean_temp_c"]),
        "drought_risk": r["drought_risk"],
        "heat_risk": r["heat_risk"]
    }