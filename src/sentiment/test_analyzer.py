from src.sentiment.analyzer import analyze_sentiment

# Test 1: Positive news
print("Positive:", analyze_sentiment(
    "The company reported excellent growth and record profits."
))

# Test 2: Negative news
print("Negative:", analyze_sentiment(
    "The company suffered huge losses and declining sales."
))

# Test 3: Neutral news
print("Neutral:", analyze_sentiment(
    "The company announced a meeting on Monday."
))

# Test 4: Empty text
print("Empty:", analyze_sentiment(""))