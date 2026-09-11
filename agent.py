from langchain.agents import create_agent
from langchain_ollama import ChatOllama

from tools import search_web, get_page_content


model = ChatOllama(
    model="qwen3:1.7b",
    temperature=0
)


agent = create_agent(
    model=model,
    tools=[
        search_web,
        get_page_content
    ],
    system_prompt="""
You are a research assistant.

You have two tools:

1. search_web
   Use this to search the web for relevant information.

2. get_page_content
   Use this when a search result contains a useful webpage
   and you need detailed information from that webpage.

When researching a question:

1. Search the web first.
2. Examine the search results.
3. If a useful webpage is available, read it using
   get_page_content.
4. Analyze the information you collected.
5. Give the user a clear final answer.

Do not pretend that you visited a webpage unless
get_page_content was actually used.
"""
)