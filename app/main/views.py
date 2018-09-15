from . import main
from flask import render_template, redirect, url_for, request
from flask_login import current_user
from ..models import BlogPost, Comment
from .forms import BlogPostForm, CommentForm, DeletePost
from datetime import datetime
from .. import db, photos


@main.route('/', methods=['GET', 'POST'])
def home():
    title = 'This is a blog website'
    blogs = BlogPost.query.all()
    form = CommentForm()
    if form.validate_on_submit():
        blogs = BlogPost.query.all()
        blog = BlogPost.query.get(int(form.blog_id.data))
        new_comment = Comment(content=form.content.data, likes=0,
                              dislikes=0, time=datetime.utcnow().strftime("%H:%M"), blog=blog)
        new_comment.save_blog(new_comment)
        comments = blog.comments.all()
        return render_template('index.html', title=title, blogs=blogs, form=form, comments=comments)
    return render_template('index.html', title=title, blogs=blogs, form=form)


@main.route('/dashboard', methods=['GET', 'POST'])
def dashboard():
    title = 'Dashboard'
    blogs = BlogPost.query.all()
    form = BlogPostForm()
    del_form = DeletePost()
    if del_form.validate_on_submit():
        blog_id = int(del_form.post_id.data)
        del_blog = BlogPost.query.get(blog_id)
        del_blog.delete_blog(del_blog)
    if form.validate_on_submit():
        new_blog = BlogPost(title=form.title.data,
                            content=form.content.data,
                            category=form.category.data,
                            likes=0,
                            dislikes=0,
                            rating=0,
                            time=datetime.utcnow().strftime("%H:%M"),
                            author=current_user)
        if 'photo' in request.files:
            filename = photos.save(request.files['photo'])
            path = f'photos/{filename}'
            new_blog.image = path
        new_blog.save_blog(new_blog)

        return redirect(url_for('main.dashboard'))
    return render_template('dashboard.html', title=title, form=form, blogs=blogs, del_form=del_form)
