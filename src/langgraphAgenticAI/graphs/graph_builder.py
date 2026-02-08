# Import modules 
from langgraph.graph import StateGraph, START, END

# Local dependencies/modules 
from src.langgraphAgenticAI.states.state import State
from src.langgraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode

class GraphBuilder:
    def __init__(self, model):
        self.llm = model
        self.graph_builder = StateGraph(State)

    def basic_chatbot_build_graph(self):
        """
        Builds a basic chatbot graph using LangGraph.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph. The chatbot node is set as both 
        the entry and exit point of the graph.
        """
        
        # Initialize Basic Chatbot 
        self.basic_chatbot_node = BasicChatbotNode(self.llm)

        self.graph_builder.add_node("chatbot", self.basic_chatbot_node.process)
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_edge("chatbot", END)
        
        
    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "RAG Chatbot":
            pass
        else:
            raise ValueError(f"Unknown use case: {usecase}")

        return self.graph_builder.compile()