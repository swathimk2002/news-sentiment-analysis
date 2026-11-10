import os
from dotenv import load_dotenv

from src.news.gnews import fetch_news
from src.news.processor import process_articles
from src.storage.s3 import upload_raw_news
from src.database.insert_news import insert_articles


def lambda_handler(event, context):

    load_dotenv()

    # Step 1: Fetch news from GNews
    articles = fetch_news()

    # Step 2: Store original news JSON in S3
    bucket_name = os.getenv("S3_BUCKET_NAME")

    if not bucket_name:
        raise ValueError("S3 bucket name not configured.")

    upload_raw_news(articles, bucket_name)

    # Step 3: Process articles and analyse sentiment
    df = process_articles(articles)

    # Step 4: Store processed articles in PostgreSQL
    insert_articles(df)

    print("News pipeline executed successfully!")

    return {
        "statusCode": 200,
        "body": "News pipeline executed successfully!"
    }