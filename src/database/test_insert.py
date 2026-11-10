from src.news.gnews import fetch_news
from src.news.processor import process_articles
from src.database.insert_news import insert_articles


# Step 1: Fetch news
articles = fetch_news()

# Step 2: Process articles
df = process_articles(articles)

# Step 3: Insert into PostgreSQL
insert_articles(df)