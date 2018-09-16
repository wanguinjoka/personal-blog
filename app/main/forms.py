from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField
from wtforms.validators import Required,Length,Email,EqualTo
from wtforms import ValidationError
from ..models import Blog, Contributor, Follower ,Comment, Subscribers


class BlogForm(FlaskForm):
    title = StringField('Title',validators = [Required()])
    content= TextAreaField('Content', validators=[Required()])
    submit = SubmitField('Post Blog')

class CommentForm(FlaskForm):
    comment_content = StringField('Comment', validators = [Required()])
    name = StringField('Name',validators=[Required()])
    email = StringField('Email', validators=[Required()])
    submit = SubmitField('Post Comment')

class SubscriberForm(FlaskForm):
    name = StringField('Name',validators=[Required()])
    email = StringField('Email', validators=[Required()])
    submit = SubmitField('Subscribe')
