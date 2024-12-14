from flask import Blueprint, request, render_template
from app.news import collect_news
from newsapi import NewsApiClient
import os

home_routes = Blueprint("home_routes", __name__)

api_key = os.getenv("NEWS_API")
newsapi = NewsApiClient(api_key=api_key)

@home_routes.route("/", methods=["GET", "POST"])
@home_routes.route("/home", methods=["GET", "POST"])
def index():
    articles = None

    if request.method == "POST":
        filter_type = request.form.get("filter_type")  
        topic = None
        sources = None

        if filter_type == '2':
            sources_input = request.form.get("sources")
            sources = [source.strip().lower().replace(" ", "-") for source in sources_input.split(',')]
        else:
            topics = {
                '1': 'technology',
                '2': 'health',
                '3': 'sports',
                '4': 'business',
                '5': 'entertainment'
            }
            category_choice = request.form.get("category")
            topic = topics.get(category_choice, "general")

        keyword = request.form.get("keyword")
        num_headlines = int(request.form.get("num_headlines", 5))

        articles = collect_news(topic, keyword, num_headlines, sources)

    return render_template("home.html", articles=articles)




