from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskPracticalWebapp.models import User

class RegistrationForm(FlaskForm):
    # fname = StringField(label="Forename",
    #                     validators=[DataRequired(), Length(min=3, max=30)])
    # surname = StringField(label="Surname",
    #                     validators=[DataRequired(), Length(min=3, max=30)])
    email = StringField(label='Email',validators=[DataRequired(), Email()],
                        render_kw={"autofocus": True,
                         "id": "email",
                         "type": "email",
                         "placeholder": "Email"})

    dob = DateField(label="Date of Birth", format="%Y-%m-%d")
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6, max=20)],
                                render_kw={
                                 "id": "password",
                                 "type": "password",
                                 "placeholder": "Password"})
    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')],
                                     render_kw={
                                      "id": "confirm_password",
                                      "type": "password",
                                      "placeholder": "Confirm Password"})

    submit = SubmitField('Register')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("An account with that email already exists.")




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
    email = StringField(label='Email',validators=[DataRequired(), Email()])

    dob = DateField(label="Date of Birth", format="%Y-%m-%d", render_kw={"disabled": True})
    picture = FileField("Update Profile Picture", validators=[FileAllowed(["jpg", "png"])])



    submit = SubmitField('Save')

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError("An account with that email already exists.")

class PracticalForm(FlaskForm):
    title = StringField("Practical Title", validators=[DataRequired()], render_kw={"placeholder": "Microscopy"})
    degStudy = SelectField("Degree of Study", validators=[DataRequired()], choices=["GCSE", "A Level"])
    subject = SelectField("Subject", validators=[DataRequired()], choices=["Biology", "Chemistry", "Physics"])
    equipment = TextAreaField("Equipment", validators=[DataRequired()], render_kw={"placeholder": "• Microscope slide"})
    method = TextAreaField("Method", validators=[DataRequired()], render_kw={"placeholder": "1. Use tweezers to peel a single layer of onion skin"})
    submit = SubmitField("Save Practical")

class RequestResetForm(FlaskForm):
        email = StringField(label='Email',validators=[DataRequired(), Email()])
        submit = SubmitField("Save Practical")

        def validate_email(self, email):
            user = User.query.filter_by(email=email.data).first()
            if user is None:
                raise ValidationError("No account with that email address exists. Would you like to create one?")

class ResetPasswordForm(FlaskForm):
    password = PasswordField(label='Password', validators=[DataRequired(), Length(min=6, max=20)])
    confirm_password = PasswordField(label='Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])

    submit = SubmitField("Reset password")
