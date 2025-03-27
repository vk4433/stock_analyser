import requests
from dotenv import load_dotenv
load_dotenv()
import os
import google.generativeai as genai
from duckduckgo_search import DDGS

def search_stock_news(stock):
    query = f"{stock} latest stock price"
    with DDGS() as ddgs:
        results = ddgs.news(query,max_results=10)
        return results

 
