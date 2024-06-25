from engine import client
from run import app

from .api import create_app

app = create_app()


db = client['edu_app_db']


@app.route('/api/v1/users/<user_id>', methods=['GET'])
def get_user_by_id(user_id):
    users_collection = db['users']
    user = users_collection.find_one({"_id": user_id})
    return user

@app.route('/api/v1/courses/<course_id>', methods=['GET'])
def get_course_by_id(course_id):
    courses_collection = db['courses']
    course = courses_collection.find_one

@app.route('/api/v1/courses/instructor/<instructor_id>', methods=['GET'])   
def get_courses_by_instructor(instructor_id):
    courses_collection = db['courses']
    courses = courses_collection.find({"instructor_id": instructor_id})
    return courses

@app.route('/api/v1/courses/student/<student_id>', methods=['GET'])
def get_courses_by_student(student_id):
    courses_collection = db['courses']
    courses = courses_collection.find({"students_enrolled": student_id})
    return courses

@app.route('/api/v1/enrollments/student/<student_id>', methods=['GET'])
def get_enrollments_by_student(student_id):
    enrollments_collection = db['enrollments']
    enrollments = enrollments_collection.find({"user_id": student_id})
    return enrollments

@app.route('/api/v1/enrollments/course/<course_id>', methods=['GET'])
def get_assignments_by_course(course_id):
    assignments_collection = db['assignments']
    assignments = assignments_collection.find({"course_id": course_id})
    return assignments

@app.route('/api/v1/grades/student/<student_id>', methods=['GET'])
def get_grades_by_student(student_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"user_id": student_id})
    return grades

@app.route('/api/v1/grades/assignment/<assignment_id>', methods=['GET'])
def get_grades_by_assignment(assignment_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"assignment_id": assignment_id})
    return grades

@app.route('/api/v1/grades/course/<course_id>', methods=['GET'])
def get_grades_by_course(course_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"course_id": course_id})
    return grades

@app.route('/api/v1/grades/instructor/<instructor_id>', methods=['GET'])
def get_grades_by_instructor(instructor_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"graded_by": instructor_id})
    return grades

@app.route('/api/v1/grades/student/<student_id>/course/<course_id>', methods=['GET'])
def get_grades_by_student_and_course(student_id, course_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"user_id": student_id, "course_id": course_id})
    return grades

@app.route('/api/v1/grades/student/<student_id>/assignment/<assignment_id>', methods=['GET'])
def get_grades_by_student_and_assignment(student_id, assignment_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"user_id": student_id, "assignment_id": assignment_id})
    return grades


@app.route('/api/v1/grades/course/<course_id>/assignment/<assignment_id>', methods=['GET'])
def get_grades_by_course_and_assignment(course_id, assignment_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"course_id": course_id, "assignment_id": assignment_id})
    return grades

@app.route('/api/v1/grades/student/<student_id>/course/<course_id>/assignment/<assignment_id>', methods=['GET'])
def get_grades_by_student_and_course_and_assignment(student_id, course_id, assignment_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"user_id": student_id, "course_id": course_id, "assignment_id": assignment_id})
    return grades

app.route('/api/v1/grades/instructor/<instructor_id>/course/<course_id>/assignment/<assignment_id>', methods=['GET'])
def get_assignments_by_student(student_id):
    enrollments = get_enrollments_by_student(student_id)
    course_ids = [enrollment['course_id'] for enrollment in enrollments]
    assignments = []
    for course_id in course_ids:
        course_assignments = get_assignments_by_course(course_id)
        assignments.extend(course_assignments)
    return assignments

@app.route('/api/v1/grades/instructor/<instructor_id>/course/<course_id>/assignment/<assignment_id>', methods=['GET'])
def get_grades_by_student_and_assignment(student_id, assignment_id):
    grades_collection = db['grades']
    grades = grades_collection.find({"user_id": student_id, "assignment_id": assignment_id})
    return grades




