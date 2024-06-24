from flask import Blueprint, redirect, url_for, session, render_template, current_app, flash,get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User
from app.forms import RegistrationForm, LoginForm

main = Blueprint('main', __name__)

# Define the routes for the main blueprint
@main.route('/')
def index():
    return render_template('landing.html')

@main.route('/sign-in')
def sign_in():
    return render_template('sign-in.html')

@main.route('/dash')
@login_required
def dashboard():
    return render_template('dashboard.html')

@main.route('/courses')
def courses():
    return render_template('courses.html')

@main.route('/liked_courses')
def liked_courses():
    return render_template('liked-course.html')


@main.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        name = form.name.data
        email = form.email.data
        password = form.password.data
        existing_user = User.get_by_email(email)
        if existing_user is None:
            user = User.create(email, name, email, password)
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('A user with that email already exists.')
    login_form = LoginForm()
    flash_messages = get_flashed_messages(with_categories=True)
    # return render_template('login.html', register_form=form, login_form=login_form)
    return render_template('login.html', register_form=form, login_form=form, flash_messages=flash_messages)

@main.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.get_by_email(form.email.data)
        if user and user.check_password(form.password.data):
            login_user(user)
            return redirect(url_for('main.dashboard'))
        else:
            flash('Invalid email or password.')
    register_form = RegistrationForm()
    flash_messages = get_flashed_messages(with_categories=True)
    return render_template('login.html', register_form=register_form, login_form=form, flash_messages=flash_messages)
    # return render_template('login.html', register_form=register_form, login_form=form)

# Google login

@main.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('user', None)
    return redirect(url_for('main.index'))
 