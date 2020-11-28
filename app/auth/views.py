from flask import request, flash, redirect, render_template, url_for
from flask_login import login_required, login_user, logout_user

from . import auth
#from .forms import LoginForm, RegistrationForm
from .. import db
from ..models import User


@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if (request.form["password"] == request.form["confirm_password"]):
            # user object <- form data
            user = User(
                email = request.form["email"],
                nom = request.form["nom"],
                job = request.form["job"],
                password = request.form["password"]
            )

            # add user to the database
            db.session.add(user)
            db.session.commit()

            # redirect to the login page
            flash('You have successfully registered! You may now login.', 'success')
            return redirect(url_for('auth.login'))
        else:
            flash('Les mots de passe ne correspondent pas.', 'warning')
            return redirect(url_for('auth.register'))

    # load registration template
    return render_template('auth/register.html', title='Register')


@auth.route('/', methods=['GET', 'POST'])
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = User.query.filter_by(email=request.form["email"]).first()
        if user is not None and user.verify_password(request.form["password"]):
            login_user(user)
            return redirect(url_for('home.welcome'))
        else:
            flash('Invalid email or password.', 'danger')

    # load login template
    return render_template('auth/login.html', title='Login')


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully been logged out.', 'success')
    return redirect(url_for('auth.login'))
