from flask import Blueprint, request, render_template
from app.news import collect_news, fetch_sources
from app.email_service import send_mail_with_mailgun

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/", methods=["GET", "POST"])
@home_routes.route("/home", methods=["GET", "POST"])
def index():
    articles = None
    available_sources = fetch_sources()  # Fetch sources dynamically

    if request.method == "POST":
        filter_type = request.form.get("filter_type")
        topic = None
        sources = None

        if filter_type == '2':
            selected_sources = request.form.getlist("sources")  # Retrieve selected sources
            sources = [source.strip().lower().replace(" ", "-") for source in selected_sources]
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

        send_email = request.form.get("send_email")
        if send_email == "on":
            email_address = request.form.get("email_address")
            if email_address:
                html_content = render_template("email_template.html", articles=articles)
                send_mail_with_mailgun(
                    recipient_address=email_address,
                    subject="Your Top News Snapshot",
                    html_content=html_content
                )

    return render_template("home.html", articles=articles, available_sources=available_sources)





