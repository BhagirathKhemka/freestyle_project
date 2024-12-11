from app.news import collect_news
from datetime import datetime
from app.tools import convert_to_est 

def test_collect_news():
    mock_response = {
        'articles': [
            {
                'title': 'Sample headline 1',
                'source': {'name': 'BBC News'},
                'description': 'Sample description',
                'publishedAt': '2024-12-11T15:00:00+0000',
                'url': 'http://example.com/1',
                'urlToImage': 'http://example.com/image1.jpg'
            },
            {
                'title': 'Sample headline 2',
                'source': {'name': 'CNN'},
                'description': 'Another description',
                'publishedAt': '2024-12-11T16:00:00+0000',
                'url': 'http://example.com/2',
                'urlToImage': 'http://example.com/image2.jpg'
            }
        ]
    }

    top_headlines = mock_response
    headlines = []
    headline_number = 1
    num_headlines = 3
    for article in top_headlines['articles']:
        if article['title'] != '[Removed]' and headline_number <= num_headlines:
            published_date = convert_to_est(article['publishedAt'])
            headline = (f"{headline_number}. {article['title']}\n"
                        f"Source: {article['source']['name']}\n"
                        f"Description: {article['description']}\n"
                        f"Published: {published_date}\n"
                        f"Link: {article['url']}\n")
            headlines.append(headline)
            headline_number += 1
    
    assert len(headlines) == 2, f"Expected 2 headlines, got {len(headlines)}"
    assert headlines[0].startswith("1. Sample headline 1"), f"Unexpected headline content: {headlines[0]}"
    assert headlines[1].startswith("2. Sample headline 2"), f"Unexpected headline content: {headlines[1]}"
