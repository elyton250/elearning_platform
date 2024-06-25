
"""this module contains the api endpoints for the application"""

from flask import Blueprint, redirect, url_for, session, render_template, current_app, flash,get_flashed_messages
from flask_login import login_user, logout_user, login_required, current_user
from app.models import User, Course

api_v1 = Blueprint('api_v1', __name__)




# Get Methods
@api_v1.route('/courses')
def get_all_courses():
    courses = Course.get_all_courses()
    return render_template('courses.html', courses=courses)
@api_v1.route('/courses/<course_id>')
def get_courses_by_id(course_id):
    course = Course.get_course_by_id(course_id)
    return render_template('course.html', course=course)

@api_v1.route('/users/<email>')
def get_courses_by_user(email):
    courses = User.get_user_courses(email)
    return render_template('courses.html', courses=courses)


@api_v1.route('/users')
def get_all_users():
    users = User.get_all_users()
    return render_template('users.html', users=users)


# Post Methods

@api_v1.route('/users', methods=['POST'])
def add_courses_to_user(email, course_id):
    User.add_course_to_user(email, course_id)
    return redirect(url_for('api_v1.get_courses_by_user', email=email))

