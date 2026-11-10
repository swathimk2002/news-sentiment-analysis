from src.news.gnews import fetch_news
from src.news.processor import process_articles

# Fetch latest news
articles = fetch_news()

# Process articles and analyse sentiment
df = process_articles(articles)

# Display results
print("\nProcessed Articles:")
print(df[["title", "source_name", "sentiment", "sentiment_score"]])

print("\nTotal processed articles:", len(df))
print("\nAvailable columns:")
print(df.columns.tolist())