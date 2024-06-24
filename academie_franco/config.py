import os
from dotenv import load_dotenv
from api.v1.engine import uri

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'you_should_change_this')
    MONGO_URI = f'{uri}'
