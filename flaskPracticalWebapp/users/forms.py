import re
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskPracticalWebapp.models import User

class RegistrationForm(FlaskForm):
    # Should the user have to enter their fullname upon Registration, or should
    # usernames be used - More child-friendly but less professional
    # Alternatively, allow user to enter full name and set their username to be 0000-Initials (similar to Integral)

    # fname = StringField(label="Forename",
    #                     validators=[DataRequired(), Length(min=3, max=30)])
    # surname = StringField(label="Surname",
    #                     validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email',validators=[DataRequired(), Email()],
                        render_kw={
                            "autofocus": True,
                            "id": "email",
                            "type": "email",
                            "placeholder": "Email"
                            })
    # Sort out Date format in html and when submiting forms
    dob = DateField(label="Date of Birth", format="%d/%m/%Y")
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=20)],
                                render_kw={
                                    "id": "password",
                                    "type": "password",
                                    "placeholder": "Password"
                                    })
    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')],
                                     render_kw={
                                        "id": "confirm_password",
                                        "type": "password",
                                        "placeholder": "Confirm Password"
                                        })
    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("An account with that email already exists.")

class UsernameForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(min=5, max=15))

    def validate_username(self, username):
        excluded_chars = re.compile("\W")
        ec = excluded_chars.findall(username)
        hasdigit = re.compile("\d")
        user = User.query.filter_by(username=username).first()
        if user:
            raise ValidationError("An account with that username already exists. Please try a different one")
        if ec:
            raise ValidationError(f'Special character(s) {ec} are not allowed.')
        if not(hasdigit.search(username)):
            raise ValidationError("Your username must include atleast one digit.")
class LoginForm(FlaskForm):
    email = StringField(label='Email',validators=[DataRequired(), Email()],
                        render_kw={"autofocus": True,
                         "id": "email",
                         "type": "email",
                         "placeholder": "email"})
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6, max=20)])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')

class UpdateAccountForm(FlaskForm):
    fname = StringField(label="Forename",
                        validators=[DataRequired(), Length(min=3, max=30)])
    surname = StringField(label="Surname",
                        validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    dob = DateField(label="Date of Birth", format="%Y-%m-%d", render_kw={"disabled": True})
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])
    submit = SubmitField('Save')

# Create an update settings form?

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("An account with that email already exists.")

class RequestResetForm(FlaskForm):
        email = StringField(label='Email', validators=[DataRequired(), Email()])
        submit = SubmitField("Save Practical")

        def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError("No account with that email address exists. Would you like to create one?")

class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=8, max=20)])
    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Reset password")
