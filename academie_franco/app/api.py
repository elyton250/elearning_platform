# Import necessary modules
from flask import Blueprint, jsonify, request
from flask_login import login_required
from app.models import User, Course  # Assuming these are correctly imported
from app import mongo

# Define the blueprint for API endpoints
api_v1 = Blueprint('api_v1', __name__)

# GET Methods
#
#
#
#GET Methods

@api_v1.route('/courses', methods=['GET'])
def get_all_courses():
    courses = Course.get_all_courses()
    return jsonify(courses)

@api_v1.route('/courses/<course_id>', methods=['GET'])
def get_course_by_id(course_id):
    course = Course.get_course(course_id)
    if course:
        return jsonify(course)
    else:
        return jsonify({'message': 'Course not found'}), 404

@api_v1.route('/users/<email>', methods=['GET'])
@login_required
def get_courses_by_user(email):
    courses = User.get_user_courses(email)
    return jsonify(courses)

@api_v1.route('/users', methods=['GET'])
@login_required
def get_all_users():
    users = User.get_all_users()
    return jsonify(users)

#TODO: add the get_marks_by_user method

# POST Methods
#
#
#
#
#
#
# POST METHODS 

@api_v1.route('/post_courses_to_user', methods=['POST'])
def add_course_to_user(email=None, course_id=None):
    data = request.get_json()
    email = data.get('email')
    course_id = data.get('course_id')
    if not email or not course_id:
        return jsonify({'error': 'Missing email or course_id in request'}), 400
    if not User.get_by_email_enroll(email):
        return jsonify({'error': 'Invalid email'}), 400
    if not Course.is_course_valid(course_id):
        return jsonify({'error': 'Invalid course ID'}), 400
    User.add_course_to_user(email, course_id)
    return jsonify({'message': 'Course added successfully.'})

@api_v1.route('/post_courses', methods=['POST'])
def create_course():
    data = request.get_json()
    title = data.get('title')
    description = data.get('description')
    instructor = data.get('instructor')
    lessons = data.get('lessons')
    if not title or not description or not instructor or not lessons:
        return jsonify({'error': 'Missing required fields: title, description, instructor, lessons'}), 400
    course = Course.create(title, description, instructor, lessons)
    return jsonify(course), 201


@api_v1.route('/post_marks', methods=['POST'])
def post_marks():
    data = request.get_json()
    user_email = data.get('user_email')
    course_id = data.get('course_id')
    marks = data.get('marks')
    # print('i am here', user_email, course_id, marks)
    if not user_email or not course_id or not marks:
        return jsonify({'error': 'Missing required fields: user_id, course_id, marks'}), 400
    User.add_marks_to_user(user_email, course_id, marks)
    return jsonify({'message': 'Marks added successfully.'}), 200

