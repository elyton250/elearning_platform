import os
from dotenv import load_dotenv
from api.v1.engine import uri

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you_should_change_this')
    GOOGLEee_CLIENT_IDee = os.getenv('GOOGLE_CLIENT_ID', "165315061371-6q85p06tpqdnak762n1h94lgvhrs217t.apps.googleusercontent.com")
    GOOGLEee_CLIENT_SECRETeee = os.getenv('GOOGLE_CLIENT_SECRET', "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")
    MONGO_URI = f'{uri}'
