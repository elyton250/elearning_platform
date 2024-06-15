from flask_login import UserMixin
from flask import current_app

class User(UserMixin):
    def __init__(self, id_, name, email):
        self.id = id_
        self.name = name
        self.email = email

    @staticmethod
    def get(user_id):
        user_doc = current_app.config['MONGO_CLIENT'].db.users.find_one({"_id": user_id})
        if user_doc:
            return User(user_doc["_id"], user_doc["name"], user_doc["email"])
        return None

    @staticmethod
    def create(id_, name, email):
        user_doc = {
            "_id": id_,
            "name": name,
            "email": email
        }
        current_app.config['MONGO_CLIENT'].db.users.insert_one(user_doc)
        return User(id_, name, email)
