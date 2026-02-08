import streamlit as st 
import os

# import Module created previously
from src.langgraphAgenticAI.ui.streamlitUI.uiConfigFile import Config

class LoadStreamlitUI:
    def __init__(self):
        self.config = Config()
        self.user_controls = {}

    # Create UI Components
    def load_streamlit_ui(self):
        st.set_page_config(page_title="🤖 " + self.config.get_page_title(), page_icon=":robot_face:", layout="wide")
        st.header("🤖 " + self.config.get_page_title())

        # Create the sidebar
        with st.sidebar:
            st.subheader("Customize")

            # Get options from config 
            llm_options = self.config.get_llm_options()
            usecase_options = self.config.get_usecase_options()

            # 1 - LLM selection
            self.user_controls["selected_llm"] = st.selectbox("Select LLM", llm_options, key="llm")

            if self.user_controls["selected_llm"] == "Groq":
                # Model Selection
                model_options = self.config.get_groq_model_options()
                self.user_controls["selected_groq_model"] = st.selectbox("Select Groq Model", model_options, key="groq_model")
                self.user_controls["GROQ_API_KEY"] = st.session_state["GROQ_API_KEY"] = st.text_input("Enter Groq API Key", type="password", key="groq_api_key")
                
                # Validate API Key
                if not self.user_controls["GROQ_API_KEY"]:
                    st.warning("⚠⚠⚠ Please enter your Groq API Key ⚠⚠⚠")
                else:
                    st.success("✓ Groq API Key entered successfully")

            # 2 - USE-CASE Selection
            self.user_controls["selected_usecase"] = st.selectbox("Select Use Case", usecase_options, key="usecase")

        return self.user_controls