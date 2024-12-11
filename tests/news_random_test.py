import unittest
from unittest.mock import patch, MagicMock
from datetime import datetime
import pytz

# Mock NewsApiClient class
class MockNewsApiClient:
    def __init__(self, api_key):
        self.api_key = api_key

    def get_top_headlines(self, **kwargs):
        if kwargs.get("q") == "error":
            return {"status": "error", "code": "invalid", "message": "Invalid request"}
        if kwargs.get("q") == "no-results":
            return {"status": "ok", "totalResults": 0, "articles": []}
        return {
            "status": "ok",
            "totalResults": 1,
            "articles": [
                {
                    "title": "Sample News Title",
                    "source": {"name": "Sample Source"},
                    "description": "Sample description of the news.",
                    "publishedAt": "2024-12-08T12:00:00Z",
                    "url": "https://example.com",
                    "urlToImage": "https://example.com/image.jpg",
                }
            ],
        }


class TestCollectNewsFunction(unittest.TestCase):
    @patch("builtins.print")  # Mock print to suppress output during tests
    def setUp(self, mock_print):
        self.api_key = "fake_api_key"
        self.newsapi = MockNewsApiClient(api_key=self.api_key)

    def convert_to_est(self, published_at):
        utc_time = datetime.strptime(published_at, "%Y-%m-%dT%H:%M:%SZ")
        est_tz = pytz.timezone("US/Eastern")
        est_time = utc_time.astimezone(est_tz)
        return est_time.strftime("%B %d, %Y %I:%M %p EST")

    def collect_news(self, topic, keyword, num_headlines, sources=None):
        if sources:
            top_headlines = self.newsapi.get_top_headlines(
                q=keyword or None,
                sources=",".join(sources),
                language="en",
            )
        else:
            top_headlines = self.newsapi.get_top_headlines(
                q=keyword or None, category=topic, language="en"
            )

        if top_headlines.get("status") == "error":
            raise ValueError(f"API Error: {top_headlines.get('message')}")

        headline_number = 1
        headlines = []

        for article in top_headlines.get("articles", []):
            if article["title"] != "[Removed]" and headline_number <= num_headlines:
                published_date = self.convert_to_est(article["publishedAt"])
                headline = {
                    "title": article["title"],
                    "source": article["source"]["name"],
                    "description": article["description"],
                    "published_date": published_date,
                    "link": article["url"],
                }
                headlines.append(headline)
                headline_number += 1

        return headlines

    def test_valid_inputs(self):
        headlines = self.collect_news("general", "technology", 1)
        self.assertEqual(len(headlines), 1)
        self.assertIn("title", headlines[0])
        self.assertIn("source", headlines[0])
        self.assertIn("description", headlines[0])

    def test_no_results(self):
        headlines = self.collect_news("general", "no-results", 1)
        self.assertEqual(len(headlines), 0)

    def test_invalid_request(self):
        with self.assertRaises(ValueError) as context:
            self.collect_news("general", "error", 1)
        self.assertIn("Invalid request", str(context.exception))

    def test_sources_filtering(self):
        headlines = self.collect_news("general", "technology", 1, sources=["bbc-news"])
        self.assertEqual(len(headlines), 1)
        self.assertEqual(headlines[0]["source"], "Sample Source")


# Run tests
if __name__ == "__main__":
    unittest.main()
