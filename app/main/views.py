from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db
from ..models import Contributor, Blog
from flask_login import login_required,current_user
from .forms import BlogForm

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    blogs = Blog.get_all_blogs()
    # comments = Comment.query.all()
    return render_template('index.html', blogs = blogs)

@main.route('/blog/new', methods =['GET','POST'])
@login_required
def new_blog():
    blog_form = BlogForm()
    if blog_form.validate_on_submit():
        blog = Blog(title=blog_form.title.data, content=blog_form.content.data, author=current_user)
        db.session.add(blog)
        db.session.commit()
        flash('Your Blog has been created!', 'success')
        return redirect(url_for('main.index'))


    return render_template("create_blog.html", blog_form = blog_form)
