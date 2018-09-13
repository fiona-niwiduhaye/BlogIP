from . import main
from flask import render_template


@main.route('/')
def home():
    title = 'This is a blog website'
    return render_template('index.html', title=title)
