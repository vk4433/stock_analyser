import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
import os 
from agents.news import search_stock_news
from agents.stock_price import get_stock_price

genai.configure(api_key=os.getenv("gemini"))
model = genai.GenerativeModel(model_name="gemini-1.5-flash-002")

def analysing_stock (news,stock_price):
    prompt = f"""
    You are a financial expert skilled in stock market analysis. Analyze the relationship between recent stock prices and news sentiment.

    ### Inputs:
    - **Stock Prices:** {stock_price}
    - **News Headlines:** {news}

    ### Instructions:
    1. Identify trends in the stock price (upward, downward, or stable).
    2. Analyze whether the news sentiment is positive, negative, or neutral.
    3. Correlate news sentiment with stock price movements.
    4. Provide insights on potential future price direction based on the analysis.
    5.explain all the details and also mention the data in the tabular format
    6.if the input is not related stocks replay them as i dont have imformation about the topic you are asking for


    Be concise, data-driven, and objective.
    """
    try:
        response = model.generate_content(prompt).text
        return response
    except Exception as e:
        return f"Error analyzing stock trends: {e}"


