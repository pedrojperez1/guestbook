from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from wtforms.validators import DataRequired

class GuestbookEntryForm(FlaskForm):
    """Form for adding GuestbookEntry"""
    name = StringField('Name | Nombre', validators=[DataRequired()])
    message = TextAreaField('Message | Mensaje', validators=[DataRequired()])