from src.langgraphAgenticAI.states.state import State

class BasicChatbotNode:
    """
    Basic Chatbot login implementation
    """
    def __init__(self, model):
        self.llm = model

    def process(self, state:State)-> dict:
        """
        Preprocess the input state and generates a chatbot responses
        """
        # Generate LLM response from state messages
        return {"messages": self.llm.invoke(state['messages'])}