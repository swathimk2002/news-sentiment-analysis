import pandas as pd
from src.sentiment.analyzer import analyze_sentiment


def process_articles(articles):
    """Clean news articles and analyse their sentiment."""

    processed_articles = []

    for article in articles:

        title = article.get("title") or ""
        description = article.get("description") or ""

        # Combine title and description
        text = title + " " + description

        # Analyse sentiment
        sentiment_result = analyze_sentiment(text)

        source = article.get("source") or {}

        processed_article = {
            "id": article.get("url"),
            "title": title,
            "description": description,
            "content": article.get("content"),
            "url": article.get("url"),
            "image": article.get("image"),
            "published_at": article.get("publishedAt"),
            "language": "en",
            "source_name": source.get("name"),
            "source_url": source.get("url"),
            "source_country": source.get("country"),
            "sentiment": sentiment_result["label"],
            "sentiment_score": sentiment_result["score"]
        }

        processed_articles.append(processed_article)

    return pd.DataFrame(processed_articles)