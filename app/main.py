from app.news import get_user_topic, collect_news

def main():
    topic, keyword, num_headlines, sources = get_user_topic()
    headlines = collect_news(topic, keyword, num_headlines, sources)

if __name__ == "__main__":
    main()