from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

class GuestbookEntryForm(FlaskForm):
    """Form for adding GuestbookEntry"""
    name = StringField('Your name / Tu nombre', validators=[DataRequired()])
    message = TextAreaField('Your message / Tu mensaje', validators=[DataRequired()])