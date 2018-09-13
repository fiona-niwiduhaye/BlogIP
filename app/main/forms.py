
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, TextField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length


class BlogPostForm(FlaskForm):
    title = StringField('Pitch title', validators=[
                        DataRequired(), Length(min=2, max=100)])
    content = TextAreaField('Enter Pitch Here', validators=[
        DataRequired(), Length(min=2, max=2000)])
    category = SelectField('Category', choices=[
                           ('Art', 'Art'), ('Business', 'Business'), ('Medicine', 'Medicine'), ('Music', 'Music')])
    submit = SubmitField('Publish')
