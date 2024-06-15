from flask import Blueprint, redirect, url_for, session, render_template, current_app
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User

main = Blueprint('main', __name__)




# Define the routes for the main blueprint
@main.route('/')
def index():
    return render_template('landing.html')


@main.route('/dash')
def dashboard():
    # if current_user.is_authenticated:
        # return f'Hello, {current_user.name}!'
        return render_template('dashboard.html')
    # else:
    #     return render_template('landing.html')


@main.route('/courses')
def courses():
    return render_template('courses.html')


@main.route('/liked_courses')
def liked_courses():
    return render_template('liked-course.html')



# login and logout routes
@main.route('/login')
def login():
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
