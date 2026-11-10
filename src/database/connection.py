
import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():

    db_host = os.getenv("DB_HOST", "localhost")

    connection = psycopg2.connect(
        host=db_host,
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

    return connection
