from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, SelectField
from wtforms.validators import DataRequired, Length

class PracticalForm(FlaskForm):
    # Set limit on length of Title
    title = StringField("Practical Title", validators=[DataRequired(), Length(max=60)], render_kw={"placeholder": "Microscopy"})
    degStudy = SelectField("Degree of Study", validators=[DataRequired()], choices=["GCSE", "A Level"])
    subject = SelectField("Subject", validators=[DataRequired()], choices=["Biology", "Chemistry", "Physics"])
    equipment = TextAreaField("Equipment", validators=[DataRequired()], render_kw={"placeholder": "• Microscope slide"})
    method = TextAreaField("Method", validators=[DataRequired()], render_kw={"placeholder": "1. Use tweezers to peel a single layer of onion skin"})
    submit = SubmitField("Save Practical")
