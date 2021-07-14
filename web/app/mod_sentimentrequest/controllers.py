from flask import (
        Blueprint,
        request,
        render_template,
        redirect,
        url_for
    )

from app.mod_sentimentrequest.forms import SentimentRequestForm

mod_sentimentrequest = Blueprint(
        'sentimentrequest', __name__, url_prefix='/sentimentrequest')


@mod_sentimentrequest.route('/', methods=['GET', 'POST'])
def sentimentrequest():
    form = SentimentRequestForm(request.form)

    if form.validate_on_submit():
        return redirect(url_for('home.home'))

    return render_template('sentimentrequest/sentimentrequest.html', form=form)
