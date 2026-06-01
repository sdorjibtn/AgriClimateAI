def generate_advice(question: str, crop: str | None = None, location: str | None = None) -> dict:
    question_lower = question.lower()

    advice = "Thank you for your question. AgriClimateAI is currently in prototype mode."

    if "maize" in question_lower or crop == "maize":
        advice = (
            "Maize generally requires warm conditions, adequate rainfall, and well-drained soil. "
            "For Bhutan, suitability depends strongly on elevation, rainfall timing, and temperature. "
            "Farmers should avoid waterlogged fields and consider drought-tolerant varieties where rainfall is unreliable."
        )

    elif "rice" in question_lower or crop == "rice":
        advice = (
            "Rice requires reliable water availability, warm temperatures, and suitable lowland or terraced conditions. "
            "Climate risks include delayed monsoon rainfall, heat stress during flowering, and water shortage."
        )

    elif "potato" in question_lower or crop == "potato":
        advice = (
            "Potato is generally better suited to cooler environments. "
            "High temperatures may reduce tuber formation, while excessive rainfall can increase disease risk."
        )

    elif "climate" in question_lower or "rainfall" in question_lower:
        advice = (
            "Climate information can support crop planning by identifying rainfall patterns, temperature risks, "
            "drought-prone periods, and future suitability changes."
        )

    return {
        "question": question,
        "crop": crop,
        "location": location,
        "advice": advice,
        "note": "This is a prototype response. Future versions will connect to climate data, crop models, and AI."
    }