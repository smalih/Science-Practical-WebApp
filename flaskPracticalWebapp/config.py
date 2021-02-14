import os
class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SERVER_NAME =  'localhost:5000'
    SQLALCHEMY_DATABASE_URI = os.environ.get("SQLALCHEMY_DATABASE_URI")
    MAIL_SERVER = "smtp.googlemail.com"
    MAIL_USE_TLS = True
    MAIL_PORT = 587
    MAIL_USERNAME = os.environ.get("EMAIL_USER")
    MAIL_PASSWORD = os.environ.get("EMAIL_PASS")

    STATIC_FOLDER = 'static'
