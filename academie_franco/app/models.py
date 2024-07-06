"""this module contains the models for the application"""

from flask_login import UserMixin
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash
from app.id_gen import generate_userID, generate_courseID
import uuid

class User(UserMixin):
    def __init__(self, id, name, email, password_hash=None, courses_id=None, courses=[]):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash
        self.courses = courses_id or []

    @staticmethod
    def get_all_users():
        users = []
        for user_doc in mongo.users.find():
            users.append(user_doc)
        return users

    @staticmethod
    def get_user_courses(email):
        user = User.get_by_email_enroll(email)
        return user['courses']
    
    
   
    @staticmethod
    def add_course_to_user(email, course_id):
        user = User.get_by_email_enroll(email)
        if user:
            if 'courses' not in user:
                user['courses'] = []
            if course_id not in user['courses']:
                user['courses'].append(course_id)
                mongo.users.update_one({"_id": user["_id"]}, {"$set": {"courses": user['courses']}})
                print("Course added to user")
            else:
                print("Course already added")
        else:
            print("User not found")

    @staticmethod
    def get(user_id):
        user_doc = mongo.users.find_one({"_id": user_id})
        if user_doc:
            return User(user_doc["_id"], user_doc["name"], user_doc["email"], user_doc.get("password_hash"))
        return None


     # this function is used when enrolling a user to a course
    @staticmethod
    def get_by_email_enroll(email):
        user_doc = mongo.users.find_one({"email": email})
        if user_doc:
            return user_doc
        return None
    
    #this function is used to get a user by email in login
    def get_by_email(email):
        user_doc = mongo.users.find_one({"email": email})
        if user_doc:
            return User(user_doc["_id"], user_doc["name"], user_doc["email"], user_doc["password_hash"])
        return None

    @staticmethod
    def create(name, email, password):
        _id = generate_userID()
        password_hash = generate_password_hash(password)
        user_doc = {
            "_id": _id,
            "name": name,
            "email": email,
            "password_hash": password_hash,
            "courses": [],
        }
        mongo.users.insert_one(user_doc)
        return User(_id, name, email, password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

# this the course model
#
#
#
#
#
#
#
#
#
#
#thr course model starts here
class Course:
    def __init__(self, id, title, description=None, instructor=None, modules=None):
        self.id = id
        self.title = title
        self.description = description
        self.instructor = instructor
        self.modules = modules

    @staticmethod
    def get_course(course_id):
        course_doc = mongo.courses.find_one({'course_id': course_id})
        if not course_doc:
            return None
        return course_doc
    @staticmethod
    def is_course_valid(course_id):
        return Course.get_course(course_id) is not None

# class Course:
#     def __init__(self, id, title, description, instructor_id, modules):
#         self.id = id
#         self.title = title
#         self.description = description
#         self.instructor_id = instructor_id
#         self.modules = modules
        
    def is_course_valid(course_id):
        course = Course.get_course(course_id)
        return course is not None
    @staticmethod
    def get_all_courses():
        courses = []
        for course_doc in mongo.courses.find():
            courses.append(course_doc)
        return courses

    @staticmethod
    def get_course(course_id):
        course_doc = mongo.courses.find_one({"_id": course_id})
        if course_doc:
            return course_doc
            # return Course(
            #     course_doc["_id"],
            #     course_doc["title"],
            #     course_doc["description"],
            #     # course_doc["instructor"],
            #     course_doc["modules"]
            # )
        return None
    
    @staticmethod
    def get_course_by_name(title):
        course_doc = mongo.courses.find_one({"title": title})
        if course_doc:
            return Course(
                course_doc["_id"],
                course_doc["title"],
                course_doc["description"],
                course_doc["instructor"],
                course_doc["modules"]
            )
    @staticmethod        
    def get_course_by_instructor(instructor):
        course_doc = mongo.courses.find_one({"instructor": instructor})
        if course_doc:
            return Course(
                course_doc["_id"],
                course_doc["title"],
                course_doc["description"],
                course_doc["instructor_id"],
                course_doc["modules"]
            )
        return None

    @staticmethod
    def create(title, description, instructor, lessons):
        _id = generate_courseID()
        course_doc = {
            "title": title,
            "description": description,
            "instructor_id": instructor,
            "modules": lessons
        }
        mongo.db.courses.insert_one(course_doc)
        return Course(_id, title, description, instructor, lessons)
 