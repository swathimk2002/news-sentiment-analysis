
from src.news.gnews import fetch_news
from src.storage.s3 import upload_raw_news
import os
from dotenv import load_dotenv


load_dotenv()

articles = fetch_news()

bucket_name = os.getenv("S3_BUCKET_NAME")

if not bucket_name:
    raise ValueError("S3_BUCKET_NAME not configured in .env")

upload_raw_news(articles, bucket_name)

print("S3 upload test completed successfully!")
