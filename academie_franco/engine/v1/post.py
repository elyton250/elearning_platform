from engine import client
from flask import request, jsonify
from .api import create_app

app = create_app()


db = client['edu_app_db']

@app.route('/api/v1/post_courses', methods=['POST'])
def post_course(course_data):
    courses_collection = db['courses']
    result = courses_collection.insert_one(course_data)
    return result.inserted_id

@app.route('/api/v1/enrollments', methods=['POST'])
def post_enrollment(enrollment_data):
    enrollments_collection = db['enrollments']
    result = enrollments_collection.insert_one(enrollment_data)
    return result.inserted_id