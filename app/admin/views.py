from flask import render_template,redirect,url_for,flash,request
from flask_login import login_user, current_user, logout_user,login_required
from . import admin
from .. import db,bcrypt
from ..models import Contributor
from .forms import LoginForm,RegistrationForm

@admin.route('/register', methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        contributor = Contributor(email = form.email.data,
                    name = form.name.data,
                    password = form.password.data)
        db.session.add(contributor)
        db.session.commit()

        flash('Your account has been created! You are now able to log in', 'success')

        title = "New Account"
        return redirect(url_for('admin.login'))


    return render_template('admin/register.html', registration_form=form)

@admin.route('/login',methods=['GET','POST'])
def login():

    login_form = LoginForm()
    if login_form.validate_on_submit():
        contributor = Contributor.query.filter_by(email = login_form.email.data).first()
        if contributor is not None and contributor.verify_password(login_form.password.data):
            login_user(contributor,login_form.remember.data)
            return redirect(request.args.get('next') or url_for('main.new_blog'))
        else:
            flash('Invalid Email or Password')

    title ="Login to My Blog"
    return render_template('admin/login.html',login_form = login_form,title=title)

@admin.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))
