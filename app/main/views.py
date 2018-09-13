from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from .. import db
from ..models import Follower
from flask_login import login_required,current_user
# from .forms import 

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    # pitchs =Pitch.query.all()
    # comments = Comment.query.all()
    return render_template('index.html')
