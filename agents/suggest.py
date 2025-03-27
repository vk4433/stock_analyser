import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os 
from agents.analyse import analysing_stock
from agents.news import search_stock_news
from agents.stock_price import get_stock_price
genai.configure(api_key=os.getenv("gemini"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash-002")

def suggestion (text):
    prompt = f"""
    You are a financial expert skilled in stock market analysis. Based on the provided analysis, determine the investment risk level (**high, moderate, or low**) and provide key company insights.

    ### Inputs:
    - **Analysis Text:** {text}

    ### Instructions:
    1. Summarize the key takeaways from the analysis.
    2. Assess the investment risk level (**high, moderate, or low**) and provide a **percentage-based risk score** (e.g., 70% high risk).
    3. Give a **brief company overview**, including industry, market position, and recent performance.
    4. Offer an **objective investment recommendation**, balancing potential risks and rewards.
    5. Keep the information **concise yet detailed** for quick decision-making.

    Be **data-driven, unbiased, and to the point**.
    """
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating investment suggestion: {e}"


