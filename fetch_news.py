
import os
import requests
from dotenv import load_dotenv


def fetch_news():
    """Fetch the latest technology news from GNews API."""

    # Load API key from .env file
    load_dotenv()
    api_key = os.getenv("GNEWS_API_KEY")

    if not api_key:
        print("API key not found. Check your .env file.")
        return

    # GNews API URL
    url = "https://gnews.io/api/v4/search"

    # Parameters for the API request
    params = {
        "q": "technology",
        "lang": "en",
        "max": 5,
        "apikey": api_key
    }

    # Send request to GNews
    response = requests.get(url, params=params, timeout=20)

    print("Status code:", response.status_code)

    if response.status_code == 200:
        data = response.json()
        articles = data.get("articles", [])

        print("Articles received:", len(articles))

        for article in articles:
            print("\nTitle:", article.get("title"))
            print("Source:", article.get("source", {}).get("name"))
    else:
        print("Failed to fetch news.")
        print("Error:", response.text)


if __name__ == "__main__":
    fetch_news()
