from langgraph.graph import StateGraph, START, END
from typing import TypedDict
from agents.news import search_stock_news
from agents.stock_price import get_stock_price
from agents.analyse import analysing_stock
from agents.suggest import suggestion


# Define WorkflowState
class WorkflowState(TypedDict):
    company: str
    days: str
    text: str
    news_get:str
    stock_priced:str
    stock: str

# News Extraction Agent
def news_extract(state: WorkflowState) -> WorkflowState:
    news_get = search_stock_news(state["company"])
    state["news_get"] = news_get if news_get else "No news available"
    return state

# Stock Price Extraction Agent
def stock_price_extract(state: WorkflowState) -> WorkflowState:
    state["stock_priced"] = get_stock_price(state["company"], state["days"])
    return state

# Analysis Agent
def analyze_stock(state: WorkflowState) -> WorkflowState:
    state["text"] = analysing_stock(state["news_get"], state["stock_priced"])
    return state

# Suggestion Agent
def generate_suggestion(state: WorkflowState) -> WorkflowState:
    state["stock"] = suggestion(state["text"])
    return state

# Create LangGraph Workflow
def create_workflow():
    graph = StateGraph(WorkflowState)

    # Add nodes
    graph.add_node("news", news_extract)
    graph.add_node("stock_price", stock_price_extract)
    graph.add_node("analysis", analyze_stock)
    graph.add_node("suggestion", generate_suggestion)

    # Define edges
    graph.add_edge(START, "news")
    graph.add_edge("news", "stock_price")
    graph.add_edge("stock_price", "analysis")
    graph.add_edge("analysis", "suggestion")
    graph.add_edge("suggestion", END)

    # Compile the workflow
    app = graph.compile()
    return app
