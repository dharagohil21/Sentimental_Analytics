from flask import Blueprint, render_template


mod_home = Blueprint('home', __name__, url_prefix='/home')


@mod_home.route('/', methods=['GET', 'POST'])
def home():
    return render_template("home/home.html")
