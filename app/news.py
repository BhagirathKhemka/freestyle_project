from app.tools import show_image, convert_to_est
from newsapi import NewsApiClient
from dotenv import load_dotenv
import os

load_dotenv() 

api_key = os.getenv("NEWS_API")
newsapi = NewsApiClient(api_key=api_key)

def fetch_sources():
    sources = newsapi.get_sources(language="en", country="us")
    return [source['name'] for source in sources['sources']]

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

    headlines = []
    for article in top_headlines['articles']:
        if article['title'] != '[Removed]' and article['title'] and article['description']:
            published_at = article.get('publishedAt')
            published_date = convert_to_est(published_at) if published_at else "Unknown Date"

            headline = {
                "title": article['title'],
                "source": article['source']['name'] if article['source'] and 'name' in article['source'] else "Unknown Source",
                "description": article['description'],
                "url": article['url'],
                "urlToImage": article.get('urlToImage'),
                "publishedAt": published_date
            }
            headlines.append(headline)

            if len(headlines) >= num_headlines:
                break

    return headlines
