import streamlit as st
from src.langgraphAgenticAI.ui.streamlitUI.loadUI import LoadStreamlitUI
from src.langgraphAgenticAI.LLMs.groqLLM import GroqLLM
from src.langgraphAgenticAI.graphs.graph_builder import GraphBuilder
from src.langgraphAgenticAI.ui.streamlitUI.display_result import DisplayResultStreamlit

# Load UI
def load_langgraph_agenticAI_app():
    """
    Loads and runs the LangGraph AgenticAI applications with Streamlit UI.
    This function initialize UI...
    """
    
    # Load UI
    ui = LoadStreamlitUI()
    user_input = ui.load_streamlit_ui()

    if not user_input:
        st.error("Error: Failed to load user input from the UI.")
        return

    user_message = st.chat_input("Ask me anything...")

    if user_message:
        try:
            # Configure the LLMs
            obj_llm_config = GroqLLM(user_controls_input=user_input)
            # Load model 
            model = obj_llm_config.get_llm_models()
            if not model:
                st.error("Error: LLM model could not be initialized.")
                return
            
            # Initialize and Set Up Graph based on Use Case
            usecase = user_input.get("selected_usecase")
            if not usecase:
                st.error("Error: No Use Case is Selected.")
                return
            
            # Initialize Graph Builder
            graph_builder = GraphBuilder(model)
            try:
                graph = graph_builder.setup_graph(usecase)
                
                # Display Results 
                DisplayResultStreamlit(
                    usecase=usecase, 
                    graph=graph, 
                    user_message=user_message
                ).display_result()

            except Exception as e:
                st.error(f"Error: Graph Building Failed - {e}")
                return

        except Exception as e:
            st.error(f"Error: Graph Set Up Failed - {e}")
            return
    