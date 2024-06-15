import os

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you_should_change_this')
    GOOGLE_CLIENT_ID = os.getenv('GOOGLE_CLIENT_ID', "165315061371-6q85p06tpqdnak762n1h94lgvhrs217t.apps.googleusercontent.com")
    GOOGLE_CLIENT_SECRET = os.getenv('GOOGLE_CLIENT_SECRET', "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")
    MONGO_URI = os.getenv('MONGO_URI', 'mongodb://localhost:27017/academie_franco')
