import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def generate_advice(question: str, crop: str | None = None, location: str | None = None) -> dict:
    if not os.getenv("OPENAI_API_KEY"):
        return {"error": "OPENAI_API_KEY is missing. Add it to your .env file."}

    prompt = f"""
You are AgriClimateAI, a farmer-friendly agricultural and climate-smart farming advisor.

Give advice that is:
- practical
- simple
- locally relevant where possible
- cautious when information is uncertain
- suitable for farmers and extension officers

Location: {location or "Not provided"}
Crop: {crop or "Not provided"}
Question: {question}

Structure the answer using:
1. Main advice
2. Possible causes or risks
3. What the farmer should do now
4. When to contact an extension officer
"""

    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system",
                    "content": "You are AgriClimateAI, an expert in agriculture, climate risk, and farmer advisory services."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.3
        )

        advice = response.choices[0].message.content

        return {
            "question": question,
            "crop": crop,
            "location": location,
            "advice": advice,
            "source": "OpenAI-powered AgriClimateAI prototype"
        }

    except Exception as e:
        return {
            "error": str(e),
            "message": "AgriClimateAI could not generate advice."
        }