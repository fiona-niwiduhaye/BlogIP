from . import main
from flask import render_template
from flask_login import current_user


@main.route('/')
def home():
    title = 'This is a blog website'
    return render_template('index.html', title=title)
