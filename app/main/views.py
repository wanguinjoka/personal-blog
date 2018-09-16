from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db
from ..models import Contributor, Blog , Comment
from flask_login import login_required,current_user
from .forms import BlogForm, CommentForm
from flaskext.markdown import Markdown


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

@main.route('/blog/<int:id>', methods=['GET','POST'])
def blog(id):
    get_blog = Blog.query.get(id)
    get_blog_comments = Comment.get_blog_comments(id)

    if get_blog is None:
        abort(404)

    # blog_format = get_blog.blog_content
    comment_form = CommentForm()
    if comment_form.validate_on_submit():
        comment_content = comment_form.comment_content.data
        comment_name = comment_form.name.data
        comment_email = comment_form.email.data


        new_comment = Comment(comment_content = comment_content, name = comment_name, email = comment_email, blog_id=id)
        new_comment.save_comment()

        return redirect(url_for('main.blog',id=id))

    get_comments = Comment.get_blog_comments(id)

    return render_template('blog.html', get_blog=get_blog,comment_form=comment_form, get_comments=get_comments, comments_count = len(get_blog_comments))
