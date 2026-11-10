import os
import requests
from dotenv import load_dotenv


def fetch_news():
    """Fetch the latest technology news from GNews API."""

    load_dotenv()

    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        raise ValueError("GNews API key not found.")

    url = "https://gnews.io/api/v4/search"

    params = {
        "q": "technology",
        "lang": "en",
        "max": 10,
        "apikey": api_key
    }

    response = requests.get(
        url,
        params=params,
        timeout=20
    )

    response.raise_for_status()

    data = response.json()

    articles = data.get("articles", [])

    print("Articles received:", len(articles))

    return articles