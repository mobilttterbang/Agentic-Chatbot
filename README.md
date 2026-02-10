# End to End Agentic-Chatbot 🤖
My first chatbot project built with **LangGraph** (agent workflow), **Groq API** (LLM provider), and **Streamlit** (UI).

A practical learning project where I build an AI chatbot for **daily conversations + task assistance**, and prepare it to be integrated with **tools** (e.g., web search, summarizer, etc.).

---

## Why this project
I built this as my first end-to-end chatbot to learn:
- how an LLM-based chatbot is structured from backend → UI,
- how to move from “chat only” into “agentic + tool-using” flows,
- and how to ship something usable quickly while staying easy to extend.

---

## Tech stack (simple + reasons)

### 🧠 Chatbot (LLM-based)
I’m building an AI chatbot powered by an LLM for **daily tasks and conversations**.
The goal is to evolve it into a **tool-augmented agent**, for example:
- Web search (latest info)
- Text summarization (long text → short insights)
- Other utilities/tools depending on needs

### 🧩 LangGraph (agent framework)
I use LangGraph because it makes the chatbot workflow **structured and extensible**:
- easy to add new “steps” (nodes) such as tool-calling, summarizing, routing
- clearer control of the conversation flow compared to a single script
- scalable foundation when I start adding more tools and logic

### ⚡ Groq API (LLM provider)
I use Groq as the LLM provider because:
- it’s fast (good for chat UX)
- simple API integration
- flexible for experimenting with different models while learning

### 🖥️ Streamlit (front-end UI)
I use Streamlit because:
- I can build a working UI quickly (chat input/output)
- great for rapid iteration while developing
- easy to add debugging panels/toggles as the agent grows

---

## Project structure

```text
.
├── src/                 # core chatbot/agent code (graph, nodes, tools, prompts)
├── app.py               # Streamlit entrypoint (UI + graph invocation)
├── requirements.txt     # dependencies
├── walkthrough.md       # notes / how it works
└── README.md
