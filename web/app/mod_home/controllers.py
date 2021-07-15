from flask import Blueprint, render_template
from app.mod_sentimentrequest.models import SentimentRequest

mod_home = Blueprint('home', __name__, url_prefix='/home')


@mod_home.route('/', methods=['GET', 'POST'])
def home():
    sentiment_requests = SentimentRequest.query.filter_by(
            by_user_email='test@email.com')
    return render_template(
            "home/home.html", sentiment_requests=sentiment_requests)
