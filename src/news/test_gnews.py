from src.news.gnews import fetch_news

articles = fetch_news()

print("\nTesting GNews function")

print("Total articles:", len(articles))

if articles:
    print("First article title:", articles[0].get("title"))
    print("First article source:", articles[0].get("source", {}).get("name"))
else:
    print("No articles received.")