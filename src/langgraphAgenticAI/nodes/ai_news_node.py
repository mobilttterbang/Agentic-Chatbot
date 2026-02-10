import os
from datetime import datetime
from tavily import TavilyClient
from langchain_core.prompts import ChatPromptTemplate

class AINewsNode:
    def __init__(self, model):
        """
        Initialize the AINewsNode with API keys for Tavily and Groq
        """
        self.llm = model
        self.tavily_client = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
        self.state = {}

    def fetch_news(self, state: dict)-> dict:
        """
        Fetches the latest AI news using Tavily.
        """
        frequency = state["messages"][0].content.lower()
        self.state["frequency"] = frequency
        time_range_map = {'daily':'d', 'weekly':'w', 'monthly':'m', 'yearly':'y'}
        days_map = {'daily':1, 'weekly':7, 'monthly':30, 'yearly':365}

        response = self.tavily_client.search(
            query = "Top Artificial Intelligence (AI) technology news Indonesia and Globally",
            topic = "news",
            search_depth = "basic",
            time_range = time_range_map[frequency],
            max_results = 10,
            days = days_map[frequency],
            # include_domains = ["techcrunch.com","wired.com","theverge.com","reuters.com"]
        )

        state["news_data"] = response.get("results", [])
        self.state["news_data"] = state["news_data"]
        return state

    def summarize_news(self, state: dict)-> dict:
        """
        Summarizes the fetched news using LLM.
        """
        news_items = self.state["news_data"]

        prompt_template = ChatPromptTemplate.from_messages([
            (
                "system","""
                You are an expert AI news summarizer. Your task is to 
                summarize the following AI news articles with each item include:
                - Date in **YYYY-MM-DD** format in IST timezone
                - Concise sentences summary from latest news
                - Sort news by date wise (latest first)
                - Source URL as link
                Use format: 
                ### [Date]
                - [Summary](URL"""
            ), ("user", "Articles: \n{articles}")
        ])

        # Merge articles content
        articles_str = "\n\n".join(
            f"Content: {item.get('content', '')}\nURL: {item.get('url', '')}\nDate: {item.get('published_date', '')}"
            for item in news_items
        )

        response = self.llm.invoke(prompt_template.format(articles=articles_str))
        state["summary"] = response.content
        self.state["summary"] = state["summary"]
        return state
        

    def save_result(self, state):
        """
        Saves the summarized news to a file.
        """
        frequency, summary = self.state["frequency"], self.state["summary"]
        filename = f"./AINews/{frequency}_summary.md"
        with open(filename, 'w') as f:
            f.write(f"# {frequency.capitalize()} AI News Summary")
            f.write(f"\n")
            f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            f.write(f"\n")
            f.write(summary)
        state["file_path"] = filename
        return state