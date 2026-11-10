import streamlit as st
import pandas as pd
from src.database.connection import get_connection

st.set_page_config(
    page_title="News Sentiment Dashboard",
    page_icon="📰",
    layout="wide"
)

st.title("📰 Real-Time News Sentiment Dashboard")

@st.cache_data(ttl=60)
def load_articles():
    conn = get_connection()

    try:
        query = """
            SELECT title, description, url, published_at,
                   source_name, sentiment, sentiment_score
            FROM articles
            ORDER BY published_at DESC;
        """

        df = pd.read_sql_query(query, conn)
        return df

    finally:
        conn.close()


df = load_articles()

st.subheader("News Overview")

if df.empty:
    st.warning("No news articles found in the database.")
else:
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Articles", len(df))
    col2.metric("Positive", (df["sentiment"] == "positive").sum())
    col3.metric("Negative", (df["sentiment"] == "negative").sum())
    col4.metric("Neutral", (df["sentiment"] == "neutral").sum())

    st.subheader("Sentiment Distribution")

    sentiment_counts = df["sentiment"].value_counts()
    st.bar_chart(sentiment_counts)

    st.subheader("Latest News Articles")

    st.dataframe(
        df[
            [
                "title",
                "source_name",
                "published_at",
                "sentiment",
                "sentiment_score"
            ]
        ],
        use_container_width=True,
        hide_index=True
    )