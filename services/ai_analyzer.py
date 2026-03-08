import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

def analyze_sector_with_ai(sector, news_data):

    prompt = f"""
You are a financial market analyst.

Analyze trade opportunities in the {sector} sector in India.

Provide sections:
Market Trends
Growth Drivers
Risks
Trade Opportunities
"""

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

    headers = {"Content-Type": "application/json"}

    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        result = response.json()

        if "candidates" in result:
            return result["candidates"][0]["content"]["parts"][0]["text"]

    except:
        pass

    # fallback response if API fails
    return f"""
# Trade Opportunity Analysis – {sector.title()} Sector (India)

## Market Trends
The {sector} sector in India is experiencing steady growth driven by domestic demand and exports.

## Growth Drivers
- Government policies supporting industry
- Increasing global demand
- Technological innovation

## Risks
- Regulatory changes
- Global economic fluctuations
- Supply chain disruptions

## Trade Opportunities
- Expansion into export markets
- Strategic partnerships
- Investment in innovation and R&D
"""