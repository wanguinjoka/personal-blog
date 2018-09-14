from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user, current_user, logout_user,login_required
from . import auth
from .. import db,bcrypt
from ..models import Follower
from .forms import RegistrationForm,LoginForm

@auth.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        follower = Follower(email = form.email.data,
                    name = form.name.data,
                    password = form.password.data)
        db.session.add(follower)
        db.session.commit()

        flash('Your account has been created! You are now able to log in', 'success')

        title = "New Account"
        return redirect(url_for('auth.login'))


    return render_template('auth/register.html', registration_form=form)

@auth.route('/login',methods=['GET','POST'])
def login():

    login_form = LoginForm()
    if login_form.validate_on_submit():
        follower = Follower.query.filter_by(email = login_form.email.data).first()
        if follower is not None and follower.verify_password(login_form.password.data):
            login_user(follower,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.index'))
        else:
            flash('Invalid Email or Password')

    title ="Login to My Blog"
    return render_template('auth/login.html',login_form = login_form,title=title)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
