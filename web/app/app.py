from flask import Flask, render_template
from app.mod_home.controllers import mod_home as home_module
from app.mod_sentimentrequest.controllers import (
        mod_sentimentrequest as sentimentrequest_module
    )

app = Flask(__name__)

# Configurations
app.config.from_object('config')


@app.errorhandler(404)
def not_found(error):
    return render_template('errors/404.html'), 404


app.register_blueprint(home_module)
app.register_blueprint(sentimentrequest_module)
