import pandas as pd
from app.climate_engine.climate_summary import get_climate_summary


def assess_crop_suitability(crop: str, location: str) -> dict:
    climate = get_climate_summary(location)

    if "error" in climate:
        return climate

    crops = pd.read_csv("data/sample/crop_requirements.csv")

    row = crops[crops["crop"].str.lower() == crop.lower()]

    if row.empty:
        return {
            "crop": crop,
            "location": location,
            "error": "Crop not found in prototype crop database."
        }

    c = row.iloc[0]

    temp_ok = c["min_temp_c"] <= climate["mean_temp_c"] <= c["max_temp_c"]
    rain_ok = c["min_rainfall_mm"] <= climate["annual_rainfall_mm"] <= c["max_rainfall_mm"]

    if temp_ok and rain_ok:
        suitability = "Suitable"
    elif temp_ok or rain_ok:
        suitability = "Moderately suitable"
    else:
        suitability = "Less suitable"

    return {
        "crop": crop,
        "location": location,
        "suitability": suitability,
        "mean_temp_c": climate["mean_temp_c"],
        "annual_rainfall_mm": climate["annual_rainfall_mm"],
        "drought_risk": climate["drought_risk"],
        "heat_risk": climate["heat_risk"],
        "reason": (
            f"{crop} requires approximately {c['min_temp_c']}–{c['max_temp_c']}°C "
            f"and {c['min_rainfall_mm']}–{c['max_rainfall_mm']} mm rainfall."
        )
    }