from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, DateField, TextAreaField, SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flaskPracticalWebapp.models import User
# Above imports needed to be changed so that we are only dealing with appropriate ones


class PracticalForm(FlaskForm):
    title = StringField("Practical Title", validators=[DataRequired()], render_kw={"placeholder": "Microscopy"})
    degStudy = SelectField("Degree of Study", validators=[DataRequired()], choices=["GCSE", "A Level"])
    subject = SelectField("Subject", validators=[DataRequired()], choices=["Biology", "Chemistry", "Physics"])
    equipment = TextAreaField("Equipment", validators=[DataRequired()], render_kw={"placeholder": "• Microscope slide"})
    method = TextAreaField("Method", validators=[DataRequired()], render_kw={"placeholder": "1. Use tweezers to peel a single layer of onion skin"})
    submit = SubmitField("Save Practical")
