import streamlit as st
from agents.workflow import create_workflow

# Set Streamlit page config
st.set_page_config(page_title="Stock Market Analyser", layout="wide")
st.markdown("<h1 style='text-align: center; color: green;'>Stock Market Analyser</h1>", unsafe_allow_html=True)

# Layout
col1, col2, col3 = st.columns([1, 3, 1])
with col2:
    stock_name = st.text_input(label="Stock Name", placeholder="Enter the name of the stock here")
    days = st.number_input("Enter number of days for stock history", min_value=1, value=7)
    button = st.button("Search")

# Initialize session state to store results
if "result" not in st.session_state:
    st.session_state.result = None

if button:
    if stock_name:
        workflow = create_workflow()
        state = {
            "company": stock_name,
            "days": str(days),
            "news": "",          
            "stock_price": "",  
            "text": "",         
            "stock": ""         
        }
        st.session_state.result = workflow.invoke(state)   
    else:
        st.warning("Please enter a stock name to proceed.")

# Display results if available
if st.session_state.result:
    result = st.session_state.result

    if st.button("Stock Analysis"):
        st.subheader("Stock Analysis:")
        st.write(result.get("text", "No analysis available"))

    if st.button("Investment Suggestion"):
        st.subheader("Investment Suggestion:")
        st.write(result.get("stock", "No suggestion available"))
