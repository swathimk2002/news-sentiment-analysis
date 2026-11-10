
from src.database.connection import get_connection


def create_tables():

    conn = get_connection()
    cursor = conn.cursor()

    query = """
        CREATE TABLE IF NOT EXISTS articles (
            id TEXT PRIMARY KEY,
            title TEXT,
            description TEXT,
            content TEXT,
            url TEXT,
            image TEXT,
            published_at TIMESTAMPTZ,
            language VARCHAR(10),
            source_name TEXT,
            source_url TEXT,
            source_country VARCHAR(10),
            sentiment VARCHAR(20),
            sentiment_score DOUBLE PRECISION
        );
    """

    try:
        cursor.execute(query)
        conn.commit()
        print("Articles table created successfully!")

    except Exception as e:
        conn.rollback()
        print("Error creating table:", e)
        raise

    finally:
        cursor.close()
        conn.close()


if __name__ == "__main__":
    create_tables()
