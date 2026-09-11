from langchain.tools import tool
from ddgs import DDGS
import requests
from bs4 import BeautifulSoup


@tool
def search_web(query: str) -> str:
    """
    Search the web for information related to the user's question.

    Use this tool when you need to find current or external
    information from the internet.
    """

    try:
        results = DDGS().text(
            query,
            max_results=9
        )

        if not results:
            return "No search results found."

        output = []

        for result in results:
            output.append(
                f"Title: {result['title']}\n"
                f"URL: {result['href']}\n"
                f"Snippet: {result['body']}"
            )

        return "\n\n".join(output)

    except Exception as e:
        return f"Search error: {e}"


@tool
def get_page_content(url: str) -> str:
    """
    Read the content of a webpage.

    Use this tool when a search result contains a useful URL
    and you need more detailed information from that webpage.
    """

    try:
        response = requests.get(
            url,
            headers={
                "User-Agent": "Mozilla/5.0"
            },
            timeout=10
        )

        if response.status_code != 200:
            return f"Could not access the webpage. Status: {response.status_code}"

        soup = BeautifulSoup(response.text, "html.parser")

        for element in soup(["script", "style", "nav", "footer"]):
            element.decompose()

        text = soup.get_text(
            separator=" ",
            strip=True
        )

        if not text:
            return "No readable content found on this webpage."

        return text[:10000]

    except Exception as e:
        return f"Error reading webpage: {e}"