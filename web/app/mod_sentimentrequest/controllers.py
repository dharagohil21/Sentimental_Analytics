from flask import (
        Blueprint,
        request,
        render_template,
        redirect,
        url_for
    )

from app.database import db

from app.mod_sentimentrequest.models import SentimentRequest
from app.mod_sentimentrequest.forms import SentimentRequestForm

mod_sentimentrequest = Blueprint(
        'sentimentrequest', __name__, url_prefix='/sentimentrequest')


@mod_sentimentrequest.route('/', methods=['GET', 'POST'])
def sentimentrequest():
    form = SentimentRequestForm(request.form)

    if form.validate_on_submit():
        sentiment_request = SentimentRequest(
                form.keyword.data, 'test@email.com')

        db.add(sentiment_request)
        db.commit()

        return redirect(url_for('home.home'))

    return render_template('sentimentrequest/sentimentrequest.html', form=form)
