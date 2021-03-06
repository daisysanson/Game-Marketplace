from flask_wtf import FlaskForm
from wtforms import Form, StringField, IntegerField, DateField, validators
from wtforms.validators import NumberRange, ValidationError
import datetime
from wtforms.validators import InputRequired


class InputForm(FlaskForm):
    name = StringField('Name', [validators.InputRequired()])
    rating = IntegerField('Rating', [validators.NumberRange(min=0, max=5, message="Please enter a number between 0-5")])
    date_released = DateField('Date Released',[validators.InputRequired("Please enter a date")], format='%d/%m/%Y')

    def validate_date_released(self, field):
        if field.data is None:
            raise ValidationError("Please enter the date in the correct format of dd/mm/yyyy")
        if field.data > datetime.date.today() or field.data < datetime.date(1970,1,1):
            raise ValidationError("The date you typed was invalid! Please enter a date between 1st Januray 1970 and today's date")
