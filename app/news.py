from app.tools import show_image, convert_to_est
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv() 

api_key = os.getenv("NEWS_API")
newsapi = NewsApiClient(api_key=api_key)

def get_user_topic():
    print("Get your top news snapshot now!")
    print("Do you want to filter by:")
    print("1. Category (e.g., General, Technology, etc.)")
    print("2. Specific News Sources (e.g., BBC News, CNN, etc.)")
    choice = input("Enter 1 for Category or 2 for Sources (default is 1): ")

    topic, sources = None, None

    if choice == '2':
        print("Select Specific Sources (comma-separated, e.g., BBC News, CNN).")
        sources_input = input("Enter sources: ")
        sources = [source.strip().lower().replace(" ", "-") for source in sources_input.split(',')]
    else:
        print("Select a Category:")
        print("1. Technology\n2. Health\n3. Sports\n4. Business\n5. Entertainment")
        category_choice = input("Enter a number from 1-5 (default is General): ")

        topics = {
            '1': 'technology',
            '2': 'health',
            '3': 'sports',
            '4': 'business',
            '5': 'entertainment'
        }
        topic = topics.get(category_choice, "general")

    keyword = input("Enter a keyword to search for (optional): ")
    num_headlines = int(input("How many headlines would you like to see? (default is 5): ") or 5)

    return topic, keyword, num_headlines, sources

def collect_news(topic, keyword, num_headlines, sources):
    if sources:
        top_headlines = newsapi.get_top_headlines(
            q=keyword or None,
            sources=','.join(sources),
            language="en"
        )
    else:
        top_headlines = newsapi.get_top_headlines(
            q=keyword or None,
            category=topic,
            language="en"
        )

    headline_number = 1
    headlines = []

    print(f"\nTop {num_headlines} Headlines for {sources or topic.capitalize()}")
    for article in top_headlines['articles']:
        if article['title'] != '[Removed]' and headline_number <= num_headlines:
            published_date = convert_to_est(article['publishedAt'])
            headline = (f"{headline_number}. {article['title']}\n"
                        f"Source: {article['source']['name']}\n"
                        f"Description: {article['description']}\n"
                        f"Published: {published_date}\n"
                        f"Link: {article['url']}\n")
            print(headline)
            if article.get('urlToImage'):
                show_image(article['urlToImage'])
            headlines.append(headline)
            headline_number += 1

    if not headlines:
        print("No articles found for your query.")
    return headlines
