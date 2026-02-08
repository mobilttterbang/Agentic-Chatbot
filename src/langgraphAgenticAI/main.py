import streamlit as st
from src.langgraphAgenticAI.ui.streamlitUI.loadUI import LoadStreamlitUI

# Load UI
def load_langgraph_agenticAI_app():
    """
    Loads and runs the LangGraph AgenticAI applications with Streamlit UI.
    This function initialize UI...
    """

    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: LLM model could not be initialized.")
        return None

    user_message = st.chat_input("Ask me anything...")
    