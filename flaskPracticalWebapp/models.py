from flaskPracticalWebapp import db, login_manager
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from datetime import datetime
from flask_login import UserMixin
from flask import current_app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    # username = db.Column(db.String(15, unique=True))
    fname = db.Column(db.String(30), default="")
    surname = db.Column(db.String(30), default="")
    email = db.Column(db.String(120), unique=True, nullable=False)
    # Passwords will be hashed to a 60-character string
    password = db.Column(db.String(60), nullable=False)
    # Default user profile picture
    dob = db.Column(db.String(10), nullable=False)
    profile_pic = db.Column(db.String(20), nullable=False, default="default.png")
    practicals = db.relationship("Practical", backref="author", lazy=True)

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config["SECRET_KEY"], expires_sec)
        return s.dumps({"user_id": self.id}).decode("utf-8")
    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config["SECRET_KEY"])
        try:
            user_id = s.loads(token)["user_id"]
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User({self.email}', '{self.profile_pic}')"

class Practical(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), default="", nullable=False)
    degStudy = db.Column(db.String(10), default="GCSE")
    subject = db.Column(db.String(10), default="Biology")
    equipment = db.Column(db.Text, default="Temp Equipment")
    method = db.Column(db.Text, default="Temp Method")
    safety = db.Column(db.String, default="Wear safety goggles")
    # practical_data = db.relationship("Practical_Data", backref="practical", lazy=True)
    # in_var = db.Column(db.String(100), default="", nullable=False)
    # dep_var = db.Column(db.String(100), default="", nullable=False)
    # con_var = db.Column(db.String(100), default="", nullable=False)
    # default = db.Column(db.Boolean, default=True, nullable=False)
    # date_created = db.Column(db.String(10), nullable=False)
    # date_modified = db.Column(db.String(10), default="")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False, default=1)

    # def plot_practical(practical_data):
    #     Fill in numpy, pandas and matplotlib logic to plot graph
    #     Is it possinle to return a plot in a function?
    #     Plotting logic can also be done at routes

    def __repr__(self):
        return f'''
        {self.degStudy} {self.subject} - {self.title}

        {self.equipment}

        {self.method}'''

# class Practical_Data(db.Model):
#     title = db.Column(db.String(60), nullable="False")
#     graphType = db.column(db.String(4), default="Line")
#     # parent practical
#     ppractical = db.column(db.Integer, db.ForeignKey("practical.id"), nullable=False, primary_key=True)
