from . import main
from flask import render_template
from flask_login import current_user
from ..models import BlogPost


@main.route('/')
def home():
    title = 'This is a blog website'
    return render_template('index.html', title=title)


@main.route('/dashboard')
def dashboard():
    title = 'Welcome To Your Dashboard'
    blogs = BlogPost.query.all()
    return render_template('dashboard.html', title=title)
