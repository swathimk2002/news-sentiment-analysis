from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

# Create VADER analyzer object
analyzer = SentimentIntensityAnalyzer()


def analyze_sentiment(text):

    # Handle empty or missing text
    if not text or not text.strip():
        return {"label": "neutral", "score": 0.0}

    # Calculate sentiment scores
    scores = analyzer.polarity_scores(text)

    # Extract compound score
    compound = scores["compound"]

    # Classify sentiment
    if compound >= 0.05:
        label = "positive"
    elif compound <= -0.05:
        label = "negative"
    else:
        label = "neutral"

    return {"label": label, "score": compound}