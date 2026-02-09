from langchain_tavily import TavilySearch
from langgraph.prebuilt import ToolNode
import os

def get_tools():
    """
    Return the list of tools to be used in the chatbot
    """
    tools = [
        TavilySearch(max_results=3),
    ]

    return tools

def create_tool_node(tools):
    """
    Create a tool node from the list of tools
    """
    return ToolNode(tools=tools)