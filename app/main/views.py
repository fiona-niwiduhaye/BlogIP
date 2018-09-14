from . import main
from flask import render_template, redirect, url_for
from flask_login import current_user
from ..models import BlogPost
from .forms import BlogPostForm
from datetime import datetime
from .. import db


@main.route('/')
def home():
    title = 'This is a blog website'
    blogs = BlogPost.query.all()
    return render_template('index.html', title=title, blogs=blogs)


@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    title = 'Dashboard'
    # blogs = BlogPost.query.all()
    form = BlogPostForm()
    if form.validate_on_submit():
        new_blog = BlogPost(title=form.title.data,
                            content=form.content.data,
                            category=form.category.data,
                            likes=0,
                            dislikes=0,
                            rating=0,
                            time=datetime.utcnow().strftime("%H:%M"),
                            author=current_user)
        new_blog.save_blog(new_blog)
        return redirect(url_for('main.dashboard'))
    return render_template('dashboard.html', title=title, form=form)
