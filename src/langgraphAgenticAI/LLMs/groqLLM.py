import os 
import streamlit as st
from langchain_groq import ChatGroq

class GroqLLM:
    def __init__(self, user_controls_input):
        self.user_controls_input = user_controls_input

    def get_llm_models(self):
        try:
            # Extract Groq API Key & Model 
            groq_api_key = self.user_controls_input["GROQ_API_KEY"]
            groq_model = self.user_controls_input["selected_groq_model"]
            # Check if API is exits 
            if groq_api_key=='' and os.environ["GROQ_API_KEY"]=='':
                st.error("Please Enter the Groq API Key")            
            # Load Selected LLM Model 
            llm = ChatGroq(api_key=groq_api_key, model=groq_model)
        except Exception as e:
            raise ValueError("Error Loading LLM Model: ", e)
        
        return llm