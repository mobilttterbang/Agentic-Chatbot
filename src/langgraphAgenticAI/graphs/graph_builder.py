# Import modules 
from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import tools_condition

# Local dependencies/modules 
from src.langgraphAgenticAI.states.state import State
from src.langgraphAgenticAI.nodes.basic_chatbot_node import BasicChatbotNode
from src.langgraphAgenticAI.nodes.tools_chatbot_node import ChatbotWithToolNode
from src.langgraphAgenticAI.tools.search_tool import get_tools, create_tool_node

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
        
    def chatbot_with_tools_build_graph(self):
        """
        Builds a websearch chatbot graph using LangGraph.
        This method initializes a chatbot node using the 'BasicChatbotNode' class
        and integrates it into the graph. The chatbot node is set as both 
        the entry and exit point of the graph.
        """
        
        # Define Tool & Tool Node
        tools = get_tools()
        tools_node = create_tool_node(tools)

        # Initialize the model
        obj_chatbot = ChatbotWithToolNode(self.llm)
        chatbot_with_tool_node = obj_chatbot.create_chatbot(tools)

        # Add Node 
        self.graph_builder.add_node("chatbot", chatbot_with_tool_node)
        self.graph_builder.add_node("tools", tools_node)
        ## Define Conditions and direct edges 
        self.graph_builder.add_edge(START, "chatbot")
        self.graph_builder.add_conditional_edges("chatbot",tools_condition)
        self.graph_builder.add_edge("tools", "chatbot")

    def setup_graph(self, usecase: str):
        """
        Sets up the graph based on the selected use case.
        """
        if usecase == "Basic Chatbot":
            self.basic_chatbot_build_graph()
        elif usecase == "Chatbot with Web":
            self.chatbot_with_tools_build_graph()
        else:
            raise ValueError(f"Unknown use case: {usecase}")

        return self.graph_builder.compile()