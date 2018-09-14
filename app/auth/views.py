from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user, current_user, logout_user,login_required
from . import auth
from .. import db,bcrypt
from ..models import Follower
from .forms import RegistrationForm

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        follower = follower(email = form.email.data,
                    name = form.name.data,
                    password = form.password.data)
        db.session.add(follower)
        db.session.commit()

        mail_message("Welcome to myblog",
                     "email/welcome_follower",
                     follower.email,
                     follower=follower)

        title = "New Account"
        return redirect(url_for('auth.login'))


    return render_template('auth/register.html', registration_form=form)
