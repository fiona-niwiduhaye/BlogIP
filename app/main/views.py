from . import main
from flask import render_template
from flask_login import current_user
from ..models import BlogPost
from .forms import BlogPostForm


@main.route('/')
def home():
    title = 'This is a blog website'
    blogs = BlogPost.query.all()
    return render_template('index.html', title=title, blogs=blogs)


@main.route('/dashboard')
def dashboard():
    title = 'Dashboard'
    blogs = BlogPost.query.all()
    form = BlogPostForm()
    return render_template('dashboard.html', title=title, form=form)


@main.route('/dashboard/new/blog')
def new_blog():
    title = 'Dashboard'
    form = BlogPost()
    return render_template('dashboard.html', title=title, form=form)
