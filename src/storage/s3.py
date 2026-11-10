import json
import boto3
import os
from datetime import datetime, timezone
from dotenv import load_dotenv


def upload_raw_news(articles, bucket_name):

    load_dotenv()

    region = os.getenv("AWS_REGION", "ap-south-1")

    s3 = boto3.client("s3", region_name=region)

    now = datetime.now(timezone.utc)

    file_name = now.strftime(
        "raw-news/%Y/%m/%d/%H%M%S.json"
    )

    json_data = json.dumps(articles, indent=4)

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=json_data,
        ContentType="application/json"
    )

    print(f"Raw news uploaded to S3: {file_name}")