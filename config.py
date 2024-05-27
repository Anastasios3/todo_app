import os

class Config:
    SECRET_KEY = os.urandom(24)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../instance/todo_app.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
