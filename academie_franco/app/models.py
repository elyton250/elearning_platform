from flask_login import UserMixin
from app import mongo
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin):
    def __init__(self, id_, name, email, password_hash=None):
        self.id = id_
        self.name = name
        self.email = email
        self.password_hash = password_hash

    @staticmethod
    def get(user_id):
        user_doc = mongo.users.find_one({"_id": user_id})
        if user_doc:
            return User(user_doc["_id"], user_doc["name"], user_doc["email"], user_doc.get("password_hash"))
        return None

    @staticmethod
    def get_by_email(email):
        user_doc = mongo.users.find_one({"email": email})
        if user_doc:
            return User(user_doc["_id"], user_doc["name"], user_doc["email"], user_doc.get("password_hash"))
        return None

    @staticmethod
    def create(id_, name, email, password):
        password_hash = generate_password_hash(password)
        user_doc = {
            "_id": id_,
            "name": name,
            "email": email,
            "password_hash": password_hash
        }
        mongo.users.insert_one(user_doc)
        return User(id_, name, email, password_hash)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
# this the course model
class Course:
    def __init__(self, id_, title, description, instructor, lessons):
        self.id = id_
        self.title = title
        self.description = description
        self.instructor = instructor
        self.lessons = lessons

    @staticmethod
    def get_course(course_id):
        course_doc = mongo.courses.find_one({"_id": course_id})
        if course_doc:
            return Course(
                course_doc["_id"],
                course_doc["title"],
                course_doc["description"],
                course_doc["instructor"],
                course_doc["lessons"]
            )
        return None
    
    def get_by_name(title):
        course_doc = mongo.courses.find_one({"title": title})
        if course_doc:
            return Course(
                course_doc["_id"],
                course_doc["title"],
                course_doc["description"],
                course_doc["instructor"],
                course_doc["lessons"]
            )

    @staticmethod
    def create(id_, title, description, instructor, lessons):
        course_doc = {
            "_id": id_,
            "title": title,
            "description": description,
            "instructor": instructor,
            "lessons": lessons
        }
        mongo.db.courses.insert_one(course_doc)
        return Course(id_, title, description, instructor, lessons)
