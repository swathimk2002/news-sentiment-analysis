
import pandas as pd
from src.database.connection import get_connection


def insert_articles(df):

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        INSERT INTO articles (
            id, title, description, content, url, image,
            published_at, language, source_name, source_url,
            source_country, sentiment, sentiment_score
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        ON CONFLICT (id) DO NOTHING;
    """

    inserted_count = 0

    try:
        df = df.astype(object).where(pd.notna(df), None)

        for _, row in df.iterrows():
            cursor.execute(query, (
                row["id"],
                row["title"],
                row["description"],
                row["content"],
                row["url"],
                row["image"],
                row["published_at"],
                row["language"],
                row["source_name"],
                row["source_url"],
                row["source_country"],
                row["sentiment"],
                row["sentiment_score"]
            ))

            inserted_count += cursor.rowcount

        conn.commit()
        print(f"Successfully inserted {inserted_count} new articles!")

    except Exception as e:
        conn.rollback()
        print("Error inserting articles:", e)
        raise

    finally:
        cursor.close()
        conn.close()
