from flask import Blueprint, redirect, url_for, session, render_template, current_app, flash,get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Course
from app.forms import RegistrationForm, LoginForm, Enroll
from app.link_handler import get_src

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
    name = current_user.name
    user_email = current_user.email
    course_ids = User.get_user_courses(user_email)
    courses = []    
    for course_id in course_ids:
        course = Course.get_course(course_id)
        course['src'] = get_src(course['embed_link'])
        courses.append(course)
        
        # print('in routes course', course['src'])

    # print(' this is the user email', user_email)
    # print('I should print courses here', courses)
    return render_template('dashboard.html', courses=courses, name=name)

@main.route('/chat')
@login_required
def chatbot():
    return render_template('chatbot.html')

@main.route('/learning')
@login_required
def learning():
    return render_template('learning.html')


# TODO: Checck why it is not validating  
@main.route('/courses', methods=['GET', 'POST'])
def courses(email=None, course_id=None):
    enroll = Enroll()
    if enroll.validate_on_submit():
        email = enroll.email.data
        User.add_course_to_user(email, course_id)
    # print("didnt validate the form") 
    courses = Course.get_all_courses()
    return render_template('courses.html', courses=courses, enroll=enroll)

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
            user = User.create(name, email, password)
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
@main.route('/login-google')
def login_google():
    google = current_app.config['oauth_google']
    redirect_uri = url_for('main.authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@main.route('/auth/callback')
def authorize():
    google = current_app.config['oauth_google']
    token = google.authorize_access_token()
    userinfo = google.parse_id_token(token)
    user = User.get(userinfo['sub'])
    if not user:
        user = User.create(userinfo['sub'], userinfo['name'], userinfo['email'])
    session['user'] = {'id': userinfo['sub'], 'name': userinfo['name'], 'email': userinfo['email']}
    login_user(user)
    return redirect(url_for('main.dashboard'))

@main.route('/logout')
@login_required
def logout():
    logout_user()
    session.pop('user', None)
    return redirect(url_for('main.index'))
 