from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_follower(follower_id):
    return Follower.query.get(int(follower_id))

@login_manager.user_loader
def load_contributor(contributor_id):
    return Contributor.query.get(int(contributor_id))


class Follower(UserMixin,db.Model):
    __tablename__ = 'Follower'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    hash_pass = db.Column(db.String(255), nullable = False)

    # comments = db.relationship('Comment', backref='author', lazy=True)
    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)

    def set_password(self,password):
        self.hash_pass = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hash_pass,password)

class Contributor(UserMixin,db.Model):
    __tablename__ = 'contributor'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255), nullable = False)
    email = db.Column(db.String(255),unique = True, nullable = False)
    hash_pass = db.Column(db.String(255), nullable = False)

    blogs = db.relationship('Blog', backref='author', lazy=True)
    # comments = db.relationship('Comment', backref='writer', lazy=True)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.hash_pass = generate_password_hash(password)

    def set_password(self,password):
        self.hash_pass = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.hash_pass,password)

class Blog(db.Model):
    __tablename__ = 'blog'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(1000),nullable = False)
    content = db.Column(db.Text,nullable = False)
    date_posted = db.Column(db.DateTime,default=datetime.utcnow)
    blog_pic_path = db.Column(db.String(), nullable = False, default='/static/photos/blog1.jpeg')


    contributor_id = db.Column(db.Integer, db.ForeignKey('contributor.id'), nullable =False)
    comments = db.relationship('Comment', backref='blog', lazy=True)

    def save_blog(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_all_blogs(cls):
        blogs = Blog.query.order_by('-id').all()
        return blogs

    @classmethod
    def get_single_blog(cls,id):
        blog = Blog.query.filter_by(id=id).first()
        return blog


    def __repr__(self):
        return f"Blog ('{self.content}', '{self.date_posted}','{self.category_id}')"

class Comment(db.Model):
    __tablename__='comments'
    id = db.Column(db.Integer, primary_key=True)
    comment_content = db.Column(db.String())
    date_comment = db.Column(db.DateTime, nullable=False, default = datetime.utcnow)
    name = db.Column(db.String())
    email = db.Column(db.String())

    # Follower_id = db.Column(db.Integer, db.ForeignKey('Follower.id'), nullable =False)
    # contributor_id = db.Column(db.Integer, db.ForeignKey('contributor.id'), nullable =False)
    blog_id = db.Column(db.Integer, db.ForeignKey('blog.id'))


    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_blog_comments(cls,id):
        comments = Comment.query.filter_by(blog_id=id).order_by('-id').all()
        return comments

    @classmethod
    def get_single_comment(cls,id_blog,id):
        comment = Comment.query.filter_by(blog_id=id_blog,id=id).first()
        return comment

class Subscribers(db.Model):
    __tablename__='subscribers'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    email = db.Column(db.String(255))

    def save_subscribers(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def send_single_subscribers(cls,id):
        subscribers = Subscribers.query.filter_by(id=id).first()
        return subscribers
