
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TextField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class BlogPostForm(FlaskForm):
    title = StringField('Blog title', validators=[
                        DataRequired(), Length(min=2, max=100)])
    content = TextAreaField('Write New Blog Here', validators=[
        DataRequired(), Length(min=2, max=2000)])
    category = SelectField('Category', choices=[
                           ('Art', 'Art'), ('Business', 'Business'), ('Medicine', 'Medicine'), ('Music', 'Music')])
    submit = SubmitField('Publish')


class CommentForm(FlaskForm):
    content = TextAreaField('Comment', validators=[DataRequired()])
    blog_id = StringField()
    submit = SubmitField('post')


class DeletePost(FlaskForm):
    post_id = StringField('')
    submit = SubmitField('delete')
