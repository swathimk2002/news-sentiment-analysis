from src.database.connection import get_connection

try:
    conn = get_connection()
    print("PostgreSQL database connected successfully!")

    conn.close()

except Exception as e:
    print("Database connection failed:", e)